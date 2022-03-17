# suma_scripts
Simple python scripts for various purposes

cve_report.py is used to report systems that are affected by specific CVE's.

A sample report looks like:

./cve.py 
Please provide a CVE-ID:
CVE-2020-14367
{'system_id': 'sumaprx-btc.suse.de', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'sle15sp2.suse.de', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle15-sp3-installer-updates-x86_64', 'sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'canada.suse.de', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2', 'sle15-sp3-installer-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rke-ds1', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2', 'sle15-sp3-installer-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rke-ds3', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2', 'sle15-sp3-installer-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rke-ds2', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2', 'sle15-sp3-installer-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'sumaprx-cust.suse.de', 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64-proxy-4.2'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rke3.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rke1.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'sle12sp5.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sles12-sp5-updates-x86_64'], 'errata_advisories': ['SUSE-12-SP5-2021-4147']}
{'system_id': 'rke2.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'sle15sp3.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'rescuedisk.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'nginx-lb.suse.de', 'patch_status': 'AFFECTED_PATCH_APPLICABLE', 'channel_labels': ['sle-module-basesystem15-sp3-updates-x86_64'], 'errata_advisories': ['SUSE-15-SP3-2022-845']}
{'system_id': 'sle12sp4.suse.de', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'sleha12node1', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'sleha12node2', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'uaserver.lab.dus.suse.com', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'rhel8.suse.de', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'ubuntu.suse.de', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'sle12sp3.suse.de', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}
{'system_id': 'rhel7', 'patch_status': 'NOT_AFFECTED', 'channel_labels': [], 'errata_advisories': []}

AFFECTED_PATCH_INAPPLICABLE - Affected, patch available in unassigned channel
AFFECTED_PATCH_APPLICABLE - Affected, patch available in assigned channel
NOT_AFFECTED - Not affected
PATCHED - Patched

