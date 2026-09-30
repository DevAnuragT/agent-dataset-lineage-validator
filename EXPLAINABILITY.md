# Decision and Reasoning

A lineage graph passes when every edge references declared nodes and the directed graph is acyclic. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies unique node identifiers and directed source-to-target edges. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

This checks structural lineage declarations only. It cannot verify that transformations actually ran or that source data is accurate. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
