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
We have taps & targets listed in [Singer.io](https://www.singer.io/#taps) website. While this should be good enough to get an idea, it's not maintained anymore. Most of the taps/targets does not work anymore. Even the example given in their website does not work.

Also, [Meltano Hub](https://hub.meltano.com/) is another excellent place to check on the taps/target you might need. They also do a decent job of ranking each variant of a particular tap/target.

But most of their documentation is pretty focused on using taps/targets with meltano, their in-house, ELT pipeline project - Meltano. So, folks planning on using vanilla taps/targets might find it irrelevant at times.

That's where Harmony comes in, a product agnostic hub. Useful if you plan to switch to a different ELT project using singer spec or simply want to implement raw taps/targets in their project.

## How do you plan to maintain it in future?
1. As part of project, a weekly github action is run that would sync metadata of all taps and targets.
2. Will fetch README of all projects.
3. Will also try to fetch config.json used for any tap/target from repository or from readme table.


## Roadmap
[ ] Fetch metadata for projects from gitlab.com.  
[ ] Provide a health score for each repository based on fetched metadata.  
[ ] Provide an API to fetch details about any taps/targets.  


## Footnote
Organizations currently contributing to development and maintenance of singer taps and targets :
1. [Meltano](https://meltano.com/)
2. [Hotglue](https://hotglue.com/)
3. [Airbyte](https://airbyte.com/)