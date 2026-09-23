# MoveOut — Interactive UX Prototype

A self-contained HTML prototype for student move-out item redistribution, accompanying the [UX research and survey analysis](../README.md) in this repository. The interface uses Material 3-inspired components and demonstrates three participant tasks.

## Open the prototype

Download or clone the repository, then open **[moveout-prototype-m3-revised.html](moveout-prototype-m3-revised.html)** in a modern browser. GitHub's file view shows source code; download the HTML to interact with it.

No package installation, build step or backend is required. Alternatively, from the repository root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit [the local prototype](http://127.0.0.1:8000/prototype/moveout-prototype-m3-revised.html). Stop the server with `Ctrl+C`.

Google Fonts supplies the typography and Material Symbols icons, so an internet connection is recommended for the intended appearance.

## Tasks

| Task | Scenario | Main interactions |
| --- | --- | --- |
| **1 · Organise multiple items** | Moving out in two weeks | Add items from an illustrated room or individually; choose room type; edit condition, price, dimensions and transport; set pickup details; review and publish. |
| **2 · Arrange a handover** | A student has claimed a desk | Inspect the claim, exchange simulated messages, choose a pickup time and place, and see the simulated confirmation. |
| **3 · Resolve items at risk** | Moving out in three days | Open the next-step bottom sheet; choose a charity drop-off or change the price / offer the item free. |

### Task 3 details

- The next-step selector uses the same bottom-sheet styling as Task 1. Clicking the backdrop or pressing `Escape` closes it; returning from an action restores the sheet over the originating list.
- The donation page includes an illustrative map, example charity name/address, distance and drop-off hours.
- Saving a donation schedule requires confirming that the charity accepts the item and choosing a drop-off day. The item then becomes **Scheduled**.
- Changing the price, including making the item free, keeps it **At risk** until a recipient or schedule is confirmed.

## Controls and walkthrough

- Use **Task 1 / Task 2 / Task 3** at the top to switch scenarios. Switching tasks resets the scenario data.
- Use the phone interface for a participant-style walkthrough. The right-hand flow panel provides shortcuts to individual stages and seeds sample data where needed.
- **Restart this task** resets the current scenario; reloading also resets all in-memory data.
- **Palette** and **Colour mode** let reviewers compare visual treatments. The default Fresh palette uses blue-green tones, with warm deadline and risk highlights.
- In Task 1, **Use sample dimensions & transport** supplies demonstration values for recognised sample items. Participants can enter their own values instead.
- The Items view filters **Scheduled**, **Claimed**, and **Available** / **At risk** items.

## Prototype boundaries

This is a usability-testing prototype, not a deployed marketplace:

- Room images are built-in illustrations; no camera or image recognition is used.
- Messages, listings, claims and handover confirmations are simulated locally.
- The map is illustrative, not an interactive navigation service. The charity address, distance and hours are explicitly fictional examples.
- Saving a donation plan does not contact a charity or book a service.
- Dates and participants are fixed scenario data. No account, database or persistent storage is connected.
- Profile editing and some secondary actions are outside the implemented task flows.

## Implementation and checks

All CSS, JavaScript, SVG illustrations and scenario data are in the single HTML file. Edit that file directly and refresh the browser to inspect changes.

The current revision has been checked for JavaScript syntax and manually exercised in a browser for single-item and batch publishing, required item details, simulated handover confirmation, donation acceptance validation, price-change status handling, bottom-sheet return/close behaviour, and donation map visibility. A 390 px viewport check found no horizontal page overflow.

Research findings and analysis notebooks remain documented in the [repository README](../README.md) and [Survey Analysis Notes](../Survey_Analysis_Notes.md).
