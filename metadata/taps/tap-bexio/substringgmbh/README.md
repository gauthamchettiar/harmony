# tap-bexio

`tap-bexio` is a Singer tap for bexio.

> :warning: This is still a super early version with some spaghetti code, only a couple of data endpoints implemented and probably still a lot of bugs. Happy for people testing it and helping us move this Tap forward.

Bexio API Documentation: https://docs.bexio.com/ and https://docs.bexio.com/legacy/


Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Currently supported data endpoints

* [x] Contacts
    * [x] Contact Type
    * [x] Contact Group
    * [x] Titles
* [x] Sales Order Management
    * [x] Quotes (kb_offer)
    * [x] Orders (kb_order)
    * [x] Invoices (kb_invoice)
* [ ] Purchase
* [ ] Accounting
    * [x] Accounts (accounts)
    * [x] Account Groups (account_groups)
    * [x] Manual entries (accounting_journal)
* [ ] Banking
* [ ] Items & Products
* [x] Projects & Time Tracking
* [ ] Files
* [ ] Other
    * [ ] Company Profile
    * [ ] Countries
    * [ ] Languages
    * [ ] Notes
    * [ ] Payment Types
    * [ ] Permissions
    * [ ] Tasks
    * [ ] Units
    * [ ] User Management

## Installation

Set up the tap in your meltano.yml and add `TAP_BEXIO_AUTH_TOKEN` to your `.env` file. Watch out, this is just a Singer tap for Meltano. You need a working meltano project to use this code.

```bash
meltano install
meltano elt tap-bexio target-jsonl
```

## How to add more endpoints

1. Create the corresponding schema in `schemas/`.
2. Create the corresponding stream in the file `streams.py`. Path needs to be the api path of Bexio.
3. Add your new Stream to `STREAM_TYPES` array in `tap.py` and import the class as well.
