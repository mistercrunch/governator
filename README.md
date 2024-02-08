# Governator

<img width="400" src="./docs/governator.png" />

**Governator** is a data governance toolkit that allows for managing
**data access policies** (as in who as access to what) as code.

With **Governator**, you can diff, pull, push and ultimately synchronize
data access rules across different systems, namely database engines and
business intelligence tools.

## But why?

Navigating data access in today's data infrastructure stacks is
tricky. Data is spread across data warehouses,
clouds, various databases, and a multitude of BI tools,
each with its own access rules.

It's a lot to manage.

Here's what we're dealing with:

- Complex data environments that are evolving quickly
- Diverse access rules that are hard to keep straight
- Data privacy and compliance rules that simply can't be overlooked
- Conmplex yet critical auditing requirements:
  - who has access to what?
  - who **had** access to this asset last year?
  - who **gave** access to this asset to this group?
  - who should be able to grant access to these resources in the first place?

### Syncing BI tools and RDMS

Historically most BI tools would tend to use service accounts to access
RDBMS, and have their own data access policy model to expose or hide
resources within their system. But in a world with multiple BI tools, and
where some actors may need more direct access to database - for example
a data scientist that wants to connect programmatically to Snowflake, or
from Airflow or `DBT` for instance - we want to make sure that 1) they
have a consistent view and access to resources across tools, and 2) that
their identify gets carried through, regardless of the layer they hit.

### A single pane of glass

When a new data scientist joins the growth team, they'll need access to
a bunch of things, various databases, various BI tools, some s3 buckets,
... Here we're hoping you can simply add them to a group and/or assign them
some roles, and for the magic to happen automatically. Similarly, when
they change position within the company, or the roles is given a broaded
or more limited access to assets, everyone should get that access.

### The power of source control

When managed as code, data access policies get:

1. a review/approval flow, through the proven code review processes, leaving
  a trace of who granted what, who approved and merged the change, when
1. a full trace of what hapenned in time
1. complex rules and logic can be established, compiled and reviewed
1. automation: continuous integration-type jobs can be executed to trigger
  arbitrary workflow, notifications and alerts


## Information Architecture

### Data objects

* Databases
* Schemas
* Relations (views and tables)
* Row-level predicates
* Column restrictions

### Accessors (Users and service accounts)
* Users
* Groups

## Integrations

Governator is extensible, and the goal is to extend it to support a wider
array of systems. It's build with extensibility in mind and it should
be straightforward to add support to new systems.

* **File system**: as `yaml`, allowing for managing in source control. While
  you may define semantics as code, they can be materialize atomically as
  yaml in source control.
* RDBMS:
  * Snowflake
  * BigQuery
* BI tools:
  * Apache Superset
