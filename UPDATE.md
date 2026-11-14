# Open Astrology Atlas 4.1 on your Mac

## The easy way — no Terminal

1. Download **astrology-atlas-v4.html**. If you downloaded the ZIP, unzip it and find that HTML file inside **astrology-atlas-v4**.
2. Put the HTML file somewhere convenient, such as your Desktop.
3. Right-click the file → **Open With → Google Chrome**.
4. Open **Birth Portrait** to enter or save a person. Then open **Personal Companion** for the eight new tools. On a phone, tap the menu at the top left to find these pages.

This is the complete app in one file. Keep it in the same location for consistent local storage, and use Settings → Export to keep backups. No account is required. The date, city search, charts, and calendars work locally; reference links open outside sources only when selected.

To move saved profiles from an older HTML file or localhost:5173: open the old app in the same browser, choose the circular **A** settings button → **Export**. Open the new HTML app, choose **Settings & privacy → Import file**, and select that JSON backup. The two addresses have separate browser storage. Keep the backup until you have checked the imported profiles.

## If you prefer the npm project

1. Stop the old app with **Control + C** in its Terminal window.
2. Unzip **astrology-atlas-v4.zip** wherever you prefer.
3. In Terminal, type `bash ` with a space after it. Drag **start.sh** from the extracted folder into Terminal, then press Return. This supplies its actual path, wherever you placed the folder.
4. When Vite says **ready**, open **http://localhost:5173**. Keep Terminal open while using the app.

The script selects the correct directory and installs packages when needed. This option requires Node.js 22 or newer. Using the same browser and localhost:5173 address retains old saved charts and favorites. Avoid running npm commands from your Mac home folder.

## Added in version 4.1

- A visible **Start here · Guide** page and a permanent Guide button, with short task instructions, shortcuts, and a glossary.
- **Signs & Personality** for all twelve signs, with visible positive traits and challenges.
- **My personality reading** and a Personality reading tab in Birth Portrait, with date-only alternatives or a complete known-time reading.
- A 24-rune Elder Futhark library, clearly separated historical/modern meanings, reflection draws, and private saved notes.
- Rune notes are included in library backups and can be individually or collectively deleted. Existing charts stay in the browser.

## Included since version 4

- **My Sky Today:** exact personal transit peaks and orb windows, with reflection prompts and export.
- **Life timeline:** sky events and returning cycles alongside private searchable milestones.
- **Explain My Chart:** question-led readings that show the placements and aspects behind each answer.
- **Traditions:** working sidereal charts, Jyotish D1/D9/nakshatras/Vimshottari, and Chinese solar-term Four Pillars; richer Maya reference entries.
- **Relationship atlas:** partners, friends, family, and colleagues, with synastry evidence and contacts to both charts.
- **Birth-time explorer:** compare sampled possible times without assigning a guessed birth time.
- **Correspondence cabinet:** illustrated stones, colors, flowers, botanicals, and metals, with sources and saved collections.
- **Annual planner:** a printable twelve-month document and calendar export with optional reminders after importing into a calendar app.
- Full backups now include milestones, collections, and planner preferences. Creator credit remains on the app and exported cards/planners.

## Also included

- Birth Portrait for **any date**, with optional name, time, and birthplace; save several people and revisit their cards.
- A full tropical astral card with Sun, Moon, Ascendant, chart ruler, planets, houses, aspects, retrogrades, and connected interpretations when the required details are known.
- Date-only and unknown-time results show possible signs and explain missing information.
- Chinese lunar-year animal, stem, phase, lunar birthday, and leap-month handling, with Lunar New Year as the stated boundary. The solar-term Four Pillars calculator is in Personal Companion → Traditions for known birth times and places.
- Maya Tzolk’in, Haab, and Long Count under GMT 584283, with named conventions and sources.
- A separate birth calendar with filters, cultural calendar recurrences, exact Western returns where supported, and .ics export.
- Personal stones and colors tied to actual or possible chart placements, modern month birthstones, and historical ruler-metal associations. Each states its source or editorial convention; no health claims.
- Offline search across 34,215 birthplaces, card/JSON export, and a complete browser app that opens without npm.

The larger reading sizes, Aa control, encyclopedia, compatibility, sky calendar, Moon tracker, and Chart Lab remain available. Desktop and phone-size Chromium checks pass; see `VALIDATION.md` for test scope and numerical references.
