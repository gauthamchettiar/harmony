# 🎶 Harmony
[![Metadata Sync](https://github.com/gauthamchettiar/harmony/actions/workflows/actions.yml/badge.svg)](https://github.com/gauthamchettiar/harmony/actions/workflows/actions.yml)

Unofficial central hub for keeping track of singer taps and targets.

## What is singer specification?
Singer Specification is a open source standard for data exchange between two systems.

Two concepts are defined in singer spec,
1. Taps : Source from where data will be fetched from.
2. Targets : Destination where data Will be pushed into.

Singer spec defines the format in which messages should be written out by taps and consequently be read by targets. Since it only defines the format, actual implementation can be in any arbritrary language.

Refer [full specification](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md) for complete details.


## Why is a hub needed?
While there are over 400+ integrations available using singer spec, the hard truth is not all of them are maintained. So usually if anyone want to use a tap or target, they end up creating their own instead of using an existing one. 

Airbyte has excellent post on why they are not using community managed taps and targets - [Why Airbyte Is Not Built on Top of Singer](https://airbyte.com/blog/airbyte-vs-singer-why-airbyte-is-not-built-on-top-of-singer).

While this is a very valid argument, we should not discount existence of really well maintained taps/targets. But how do we find those golden eggs?

This hub should not only act as a metadata repository of all taps/targets as well as a look into how well they are maintained.

## Don't we already have a Hub for that?
We have taps & targets listed in [Singer.io](https://www.singer.io/#taps) website. While this should be good enough to get an idea, it's not maintained anymore. The state is so bad that even the example given in their homepage does not work.

Also, [Meltano Hub](https://hub.meltano.com/) is another excellent place to check on the taps/target you might need. They also do a decent job of ranking each variant of a particular tap/target.

But most of their documentation is pretty focused on using taps/targets with their in-house ELT pipeline project - Meltano. So, folks planning on using vanilla taps/targets might find it irrelevant at times.

That's where Harmony comes in, a product agnostic hub. Useful if you plan to switch to a different ELT project using singer spec or simply want to implement raw taps/targets in their project.

Harmony will not only list all available repositories, it will also list current state of them. Which will be helpful in choosing a variant for a particularly popular tap/target.

## What all metrics do you collect?
Metadata for all taps/targets are stored in [metadata](/metadata/) : 
```
metadata/
├── taps/
│   ├── crawl_status.json
│   ├── repositories.json
│   ├── tap-postgres/
│   │   ...
│   └── tap-zuora/
└── targets/
    ├── crawl_status.json
    ├── repositories.json
    ├── target-airtable/
    │   ...
    └── target-yaml/
```

Each tap/target is a seperate directory, which will include all the variants of a particular tap/target. 
```
tap-postgres/
├── MeltanoLabs
│   ├── README.md
│   ├── config_options.json
│   └── metadata.json
├── singer-io
│   ├── README.md
│   ├── config_options.json
│   └── metadata.json
└── transferwise
    ├── README.md
    ├── config_options.json
    └── metadata.json
```
Depending on whether a repository has README.md, it will be fetched. Depending on whether a repository has a sample config, it will be fetched as config_options.json.

Based on repository activity, metadata.json will be populated as -

```json
{
    "url": "https://github.com/MeltanoLabs/tap-postgres",
    "api_url": "https://api.github.com/repos/MeltanoLabs/tap-postgres",
    "account": "MeltanoLabs",
    "repo_name": "tap-postgres",
    "account_type": "organization",
    "language": "Python",
    "readme": {
        "is_present": true,
        "url": "https://raw.githubusercontent.com/MeltanoLabs/tap-postgres/master/README.md"
    },
    "sample_config": {
        "is_present": false,
        "url": null
    },
    "stats": {
        "num_stars": 10,
        "num_watchers": 10,
        "num_forks": 10,
        "num_networks": 10,
        "num_subscribers": 5,
        "num_open_issues": 30,
        "num_open_issues_30D": 11,
        "num_closed_issues": 170,
        "num_closed_issues_30D": 16,
        "num_open_pr": 11,
        "num_open_pr_30D": 8,
        "num_closed_pr": 144,
        "num_closed_pr_30D": 15
    },
    "timestamps": {
        "ts_created_at": [
            "2022-07-27T13:27:08Z"
        ],
        "ts_last_updated_at": "2023-06-25T09:35:52Z",
        "ts_last_pushed_at": "2023-08-14T16:21:42Z",
        "ts_last_open_issue_at": "2023-08-14T16:23:47Z",
        "ts_last_closed_issue_at": "2023-08-14T11:52:53Z",
        "ts_last_open_pr_at": "2023-08-14T11:52:49Z",
        "ts_last_closed_pr_at": "2023-08-14T11:52:53Z"
    }
}
```

## How do you plan to maintain it in future?
Project will be completely automated using Github actions. Metadata sync will be run weekly once, which will fetch details about any tap/target project and update the metadata. Since this does not involve any manual steps, unless there is a breaking change in github's API. this should always contain recent data on all repositories.


## Roadmap
- [ ] Fetch metadata for projects from gitlab.com.  
- [ ] Provide a health score for each repository based on fetched metadata.  
- [ ] Provide an API to fetch details about any taps/targets.  
- [ ] Provide a seach functionality. 


## Finally, Is it worth it?
Singer specification seems to be the only open data exchange format that's been widely adopted. Though the project itself has been abandoned by the original entity, it still has some life to it provided by the community builders and organizations depending on it.

Organizations currently contributing to development and maintenance of singer taps and targets -
1. [Meltano](https://meltano.com/)
2. [Hotglue](https://hotglue.com/)
3. [Airbyte](https://airbyte.com/)