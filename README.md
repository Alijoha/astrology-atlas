# Astrology Atlas 4.1

Deployment configuration for Vercel is included. See [DEPLOY.md](DEPLOY.md). Generate the optional offline HTML from source with `npm run build:standalone`.

An illustrated, browser-local astrology reference and toolkit built with React, TypeScript, Vite, Astronomy Engine, and Luxon.

For the simplest launch, open **astrology-atlas-v4.html** in Chrome. The entire app, fonts, and birthplace index are bundled in that file; no Terminal, installation, account, or API key is needed. Keep the file in a stable location and use Settings to export backups. If moving from the localhost app, export its library first, then import the JSON into the standalone app. Browser storage differs between file and localhost origins.

For development, use Node.js 22 or newer:

```sh
npm install
npm run dev
```

`npm run build` creates the production app in `dist/`. `npm run build:standalone` rebuilds the single-file app. `npm test` runs independent astronomy/calendar fixtures, uncertainty handling, DST, aspect, export, and interaction checks. `npm run test:browser` uses Playwright and an installed Chromium (`ATLAS_CHROMIUM` overrides `/usr/bin/chromium`) to test the standalone document over loopback HTTP. Mac users can use `bash start.sh`; it selects the project directory and installs dependencies on first launch. See `UPDATE.md` for upgrading the downloaded app.

The four main areas are Explore, My Charts, Compatibility, and Calendar, with dedicated Birth Portrait, Personal Companion, and Chart Lab tools. Explore starts with a daily companion and also houses the full searchable reference library. Search opens any encyclopedia topic directly using shareable hash routes. Local storage keeps saved birth profiles, favorites, journal entries, milestones, correspondence collections, planner settings, reading size, and theme preferences on the device. Settings exports or deletes the library; each chart can be exported or deleted separately. There are no analytics, external birth-detail requests, account requirements, or locked entries.

## Birth Portrait for any date

Enter any birth date from 1900 to 2099, with an optional name. Date-only portraits show possible Western placements, the Chinese lunar year/animal/phase, Maya Tzolk’in, Haab, and Long Count, and personal symbolic stones and colors. The name labels the card without changing sky calculations. Optional local time and birthplace unlock the full tropical chart, Moon, Ascendant, chart ruler, houses, aspects, and connected readings. An offline index of 34,215 cities fills coordinates and IANA time zone; the user confirms these and can enter another location manually.

The separate Birth calendar is available within the portrait and Calendar. It shows Gregorian birthdays, matching Chinese lunar birthdays, Maya 260/365-day recurrences, and exact solar/lunar returns when the birth moment is known. Filter or export individual events or the selected year's events as .ics. A February 29 birthday is not silently moved to another date; a Chinese leap-month birthday requires the same leap-month status. Profiles, full JSON records, and readable standalone astral cards can be saved/exported.

## Find your way around

Open **Start here · Guide** in the navigation or **Guide** at the top of any screen. The home page has shortcuts for Signs & Personality, My personality reading, the guide, and Runes. The guide gives task-based instructions and a glossary, including the difference between a monthly lunar return and an annual solar return.

**Signs & Personality** puts all twelve signs in one readable page selector, with visible positive traits, challenges, communication style, emotional needs, and deeper chapters. Search results for signs show the same strengths/challenges sections. **My personality reading** opens Birth Portrait directly into the new Personality reading tab and loads the first saved person when available. Date-only results preserve alternative Moon/planet signs and omit a guessed rising sign; known-time readings connect six placements with houses and aspects. Jump buttons help readers move between placements.

**Runes** includes the 24 Elder Futhark letters, separate historical name/gloss context and original modern reflection prompts, one- or three-rune draws without replacement, favorites, a private note journal, export/import, and delete controls. Uncertain names are marked, including Perthro and Kenaz/kaunan. The index uses a common 24-rune ordering ending Dagaz, Othala; no blank rune or automatic rune-to-zodiac assignment is added. Historical references are the National Museum of Denmark and Swedish History Museum. Noto Sans Runic is bundled under SIL OFL, with license in public/fonts and the production/standalone notices.

Guide, signs, and rune references need no birth information. Rune draws use browser cryptographic randomness and are modern reflection exercises, not a prediction service. All saved charts and records remain local; the new version retains the existing storage keys and adds rune reflections to the same backup/import/delete flow.

## The eight Personal Companion tools

1. **My Sky Today:** a selected-day snapshot and an exact current-to-natal transit search. Choose moving planets, a focus, 0.5°/1°/2° orb, and a 7–365-day horizon. Results show the exact peak and surrounding continuous orb window, placement evidence, symbolic reflections, and .ics export. Birth time and birthplace must be known.
2. **Life timeline:** a range of up to 366 days of selected birth cycles, exact personal contacts, Moon phases, approximate selected retrograde stations, and global eclipse peaks, alongside private milestones. Search notes by title, text, or category; delete individual notes or export/import the full library.
3. **Explain My Chart:** question-led authored synthesis for Sun/Moon/rising, relationships, work/creativity, repeated signs, and the chart ruler. Answers expose actual sign, degree, house, and aspect evidence.
4. **Traditions:** Western tropical, Lahiri/Fagan–Bradley sidereal, Jyotish D1/rāśi and D9/Navamsa, Moon nakshatra/pada, Vimshottari major/subperiods, Chinese solar-term Four Pillars, and Chinese/Maya calendar dates. Each system retains its terms and settings. Maya topics include the twenty named days, living daykeeping, Calendar Round, Wayeb, and Long Count units.
5. **Relationship atlas:** partner, friend, family, or colleague context; actual synastry, placement evidence, bidirectional whole-sign house overlays, conversation prompts, and upcoming Venus/Jupiter/Saturn contacts to each chart. Select two distinct exact-time profiles. The existing Compatibility tool retains the midpoint composite.
6. **Birth-time explorer:** choose a range on the recorded birth date and sample every 5/10/15/30 minutes. Compare Ascendant, Moon, Midheaven, and houses; retain endpoints and explicitly skip DST gaps/folds. This is an uncertainty comparison, not verified rectification. It does not overwrite the saved birth time.
7. **Correspondence cabinet:** 60 original illustrated items across twelve signs: stones, editorial colors/flowers, historical botanicals, and planetary metals. Search, filter by actual or possible chart signs, save a collection, inspect sources, and export. Collection JSON can be imported through Settings.
8. **Annual planner:** select birth cycles, personal transits, principal Moon phases, Mercury/Venus/Mars stations, and global eclipse peaks. Download a twelve-month printable HTML document (browser Print → Save as PDF) or .ics with optional standard calendar alarms. Reminders work after import into a calendar application; this offline app does not run background notifications.

Known-time tools do not invent results for date-only profiles. Full library backups include the new notes, collections, and planner settings; import merges records. Deleting an individual profile also removes its journal, milestones, and planner settings; deleting the whole library also clears the collection.

## Calculation conventions

- Astronomy Engine 2.1.19, MIT license: geocentric apparent ecliptic longitudes of date, lunar phase and illumination, seasons, rise/set, and eclipse peaks.
- Tropical zodiac, whole-sign houses, true obliquity; traditional Ascendant ruler, with modern co-rulers in the encyclopedia.
- Five major aspects with a maximum 6° orb. Calendar personal transits use a 1° snapshot at local noon. Planetary midpoint composite uses shorter-arc midpoints; composite angles/houses are unavailable.
- Mean lunar node polynomial. Approximate degree labels are not a true-node calculation.
- Luxon + browser Intl/IANA historical local civil-time conversion. DST gaps are rejected and repeated times offer a UTC offset choice. Pre-1970 time-zone histories can be incomplete and are flagged.
- Birth dates 1900–2099, latitudes 66° S to 66° N. Unknown times sample local noon, flag signs that change across the civil day, and omit houses, angles, and chart rulers.
- Without a birthplace/time zone, date-only portraits cover all possible instants of the civil date across UTC−12 to UTC+14. They show alternative signs, omit exact degrees, aspects, retrograde labels, houses, angles, and rulers, and do not draw a fabricated exact chart. Date-only profiles are excluded from synastry and exact-time Chart Lab tools.
- Chinese date conversion uses browser ICU/Intl: Lunar New Year changes the year animal, stem, and phase. Lunar month/day and leap-month status are retained. This is not the Li Chun year-pillar convention and does not claim to calculate full BaZi/Four Pillars.
- Sidereal: mean Lahiri J2000 anchor 23.857092353708822° or Fagan–Bradley 24.740299994434963°, with IAU 2006 precession polynomial and nutation in longitude from Astronomy Engine. Whole-sign houses. Navamsa uses ninefold sidereal longitude. Vimshottari uses the standard 120-year sequence and 365.25-day mean years; dates are sensitive to birth time, Moon longitude, and convention.
- Four Pillars: physical apparent solar longitude at 315° sets Li Chun; 30° jie intervals set months. Day/hour use confirmed local civil clock, with explicit midnight or 23:00 rollover. Apparent solar time and luck pillars are not calculated.
- Maya conversion uses GMT correlation 584283, proleptic Gregorian dates, a civil-midnight boundary, and common Yucatec names. Calendar designations are distinguished from Dreamspell and from universal personality predictions.
- Calendar ingresses and planetary aspects are bracketed at six-hour intervals and solved by bisection. Retrograde stations use a centered one-day longitude derivative and are approximate. Global eclipse peaks do not imply local visibility.
- Moonrise and moonset use the chosen observing coordinates, geometric horizon, and selected civil day's 24-hour interval. Terrain is not modeled.

## Availability

Tropical natal charts, planetary sky data, Moon tracking, sign comparisons, synastry, house overlays, planetary midpoint composites, solar/lunar longitude returns, secondary progressed planetary positions, Chinese year-zodiac/lunar dates, and Maya calendar dates are interactive. Return moments are independently compared with Swiss Ephemeris fixtures; Maya dates with Fourmilab and published anchors; Chinese boundary dates with Hong Kong Observatory tables. Return houses and progressed angles remain unavailable. Personal Companion adds Lahiri/Fagan–Bradley sidereal positions and houses, Jyotish D1/D9, nakshatra/pada and Vimshottari major/subperiods, and solar-term Chinese Four Pillars. Additional Jyotish divisions, Chinese luck pillars, Chiron, lots, and astrocartography remain reference-only with explicit availability notices. No unsupported system substitutes a tropical result.

## References and licenses

Astronomy Engine: https://github.com/cosinekitty/astronomy (MIT). Luxon: https://github.com/moment/luxon (MIT). React and Vite: MIT. Lucide icons: ISC. All zodiac and celestial SVG illustrations are original project artwork. Marcellus and DM Sans fonts are bundled locally under SIL Open Font License (license files in `public/fonts/`); system serif/sans-serif fallbacks are also available.

Reference entries cite Ptolemy's *Tetrabiblos*, Encyclopaedia Britannica, NASA, the GIA Gem Encyclopedia, Jewelers of America, the Hong Kong Observatory, and IANA. Associations are labeled by tradition or identified as contemporary editorial symbolism. No health claims are made for minerals. Astrological interpretations are clearly separated from calculated astronomy.

Birthplace index: GeoNames cities15000, reduced to names, region/country codes, coordinates, time zone, and population; CC BY 4.0. Attribution and source are in `public/data/GeoNames-attribution.txt`. Searches stay local. The standalone HTML also embeds runtime, font, and data license notices in its `bundled-licenses` JSON block. Maya reference entries cite Smithsonian Living Maya Time and Fourmilab.

See `VALIDATION.md` for numerical checks and end-to-end testing status. Swiss Ephemeris is used only as an optional external verification reference and is not bundled, imported, or distributed with the application.

## Interactive interpretation and reading

The reference library includes 374 searchable topics, including 132 planet/Ascendant-in-sign combinations. Twelve authored sign chapters and their 72 core placement interpretations combine with planetary-function, house, and aspect context in the explorers. Slow-moving planets explicitly include generational context. Interpretations are editorial symbolic prompts, rather than a claim that a position determines behavior.

Chart synthesis joins the calculated placements, chart ruler, close aspects, and sign/house context. Element/modality distributions count the ten planets equally; they are not personality scores. Grand trines and T-squares use the selected fixed 6° aspect convention; the sign stellium convention is three or more of the ten planets.

The Aa control sets a locally saved type scale. Most reference paragraphs use 18px at the comfortable setting, with larger settings available. Articles open in a wide, centered reader on desktop and occupy the phone screen on mobile. The journal is browser-local and included in export/import/delete controls.

## Creator

Created by **Johanna Polanco** with love ♡ · **US Army veteran**. The credit appears in the app footer, downloadable astral cards, and annual planners.
