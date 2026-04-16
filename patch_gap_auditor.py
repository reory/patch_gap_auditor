from importlib.metadata import distributions
from loguru import logger
import requests
import json
from datetime import datetime

def get_installed_inventory():
    """
    Scans the local environment and returns a dictionary of {name: version}.
    This is the inventory phase of the project.
    """

    inventory = {dist.metadata['Name']: dist.version for dist in distributions()}

    # Lets filter out the auditor and common small tools
    # to keep the report clean
    logger.info(f" Inventory complete. Found len {len(inventory)} packages to audit")
    return inventory

def run_audit(inventory):
    """Negotiate with the API and then Report the findings."""
    
    # Google OSV batch endpoint
    url = "https://api.osv.dev/v1/querybatch"

    # Formatting for the OSV API
    queries = []
    for name, version in inventory.items():
        queries.append({
            "version": version,
            "package": {"name": name, "ecosystem": "PyPI"}
        })

    logger.info("📡Querying Google OSV Database..")

    try:
        # Sending all 9 packages in one single batch request
        # Max 15secs wait
        response = requests.post(url, json={"queries": queries}, timeout=15)
        response.raise_for_status()
        results = response.json().get("results", [])

        vulnerabilities_found = 0

        # Iterate thorugh API results and local names simultaneously
        for (name, version), result in zip(inventory.items(), results):
            vulns = result.get("vulns", [])
            if vulns:
                vulnerabilities_found += len(vulns)
                logger.error(f" 🛑 {name} v{version} is Vulnerable!")

                for v in vulns:
                    # Provide a specific id and link for the fix
                    logger.warning(
                    f" {v['id']}: {v.get('summary', 'No summary available')}")
                    logger.debug(
                    f" Fix info: https://osv.dev/vulnerability/{v['id']}")
            else:
                logger.success(f" ✅ {name} v{version} is secure")

        # Summary status based on findings
        if vulnerabilities_found == 0:
            logger.success(" 🛡️ Audit complete: Your environment is up to date!")
        else:
            logger.critical(
                f"⚠️ Audit complete: Found {vulnerabilities_found} total amount!")

        # Report data and save to a JSON file
        report_data = {
            # Timestamp of when security snapshot was taken.
            "audit_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_packages": len(inventory),
            "vulnerabilities_found": vulnerabilities_found,
            "packages": inventory
        }
        # Write the data to a local file (JSON)
        with open("security_audit.json", "w", ) as f:
            json.dump(report_data, f, indent=4)
            logger.info(" 🗒️ Security report exported to security_audit.json")

    # If connection fails please investigate why
    except requests.exceptions.RequestException as e:
        logger.critical(f" 🛑 Connection failed: Please investigate {e}")

if __name__ == "__main__":

    # Gather data
    current_packages = get_installed_inventory()
    
    # Execute audit
    run_audit(current_packages)
