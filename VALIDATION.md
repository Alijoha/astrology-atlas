# Validation record

## Build and interaction verification

The production TypeScript check and Vite build pass. `npm test` executes 107 passing results across astronomy/reference, timing, app-flow, Chart Lab, Birth Portrait calculation, and Birth Portrait interaction, and Personal Companion calculation suites (including containing integration tests). The interaction suite uses React Testing Library and JSDOM against the actual app components and state; it does not substitute screenshots for assertions.

The four requested flows pass:

1. Search for Scorpio; inspect the traditional Mars and modern Pluto labels; open both planet reference pages.
2. Enter birth details, confirm the location and time zone, save the profile, inspect Moon and Ascendant, switch to the accessible position table, and open the chart ruler with its sign and house.
3. Compare two signs, switch reading categories, compare two saved charts, inspect aspect evidence and the complete aspect table, and open a planetary midpoint composite.
4. Select 8 April 2024, inspect the Moon and planetary events, switch from UTC to America/New_York, open New Moon, export the actual .ics Blob, and confirm its UTC DTSTART. Open the eight-phase Moon tracker.

Favorites, dark theme, and reading-size persistence are also verified. V2 interaction coverage includes all three Chart Lab tools, direct search into a planet-in-sign interpretation, sign placement tabs and keyboard navigation, the journal and exported journal data, and merging an imported backup without discarding existing profiles. Unknown-time behavior, changing lunar signs, DST gaps, repeated local times with offset choices, time-zone-invariant event times, conjunction/opposition detection, and ICS escaping are covered by numerical tests.

## Independent natal reference

The app uses Astronomy Engine 2.1.19, MIT licensed. A separately installed Swiss Ephemeris 2.10.3 Moshier calculation produced the fixtures in `tests/reference-charts.json`. Swiss Ephemeris is not part of the runtime dependency tree or production bundle. The optional generation script is `scripts/independent-reference.py`.

Matching settings: geocentric apparent tropical ecliptic longitude of date; whole-sign houses; exact UTC and observer coordinates in the fixture. The comparison covers the Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Ascendant, and Midheaven.

| UTC moment | Place | Maximum planetary difference | Ascendant difference | Midheaven difference |
| --- | --- | ---: | ---: | ---: |
| 2000-01-01 12:00 | Greenwich, 51.4779 N, 0 E | 0.003119° | 0.000056° | 0.000026° |
| 1995-11-07 14:30 | London, 51.5074 N, 0.1278 W | 0.002078° | 0.000021° | 0.000009° |
| 1990-06-15 12:30 | New York, 40.7128 N, 74.006 W | 0.001300° | 0.000001° | 0.000007° |
| 2024-04-08 18:00 | Sydney, 33.8688 S, 151.2093 E | 0.003235° | 0.000014° | 0.000015° |

The regression tolerances are 0.01° for planets and 0.001° for angles. These checks establish specific sample agreement, not a claim of exhaustive validation across every date and place.

## Independent event reference

NASA's published UTC principal-phase table gives:

- Last Quarter: 2 April 2024, 03:15 UTC
- New Moon: 8 April 2024, 18:21 UTC
- First Quarter: 15 April 2024, 19:13 UTC
- Full Moon: 23 April 2024, 23:49 UTC
- March equinox: 20 March 2024, 03:06 UTC

The application agrees within 90 seconds for each, using a geocentric model. NASA reference: https://eclipse.gsfc.nasa.gov/SKYCAL/SKYCAL.html. The April 8 global total solar eclipse is present. Global eclipse peaks are explicitly distinct from local visibility and contact times.

## Desktop and phone-size browser verification

The actual standalone HTML was tested in headless Chromium at 1440×1000 desktop and 390×844 phone viewports using `scripts/browser-qa.mjs`. All four requested flows passed in the browser: Scorpio → Mars/Pluto; exact birth details → Moon/Ascendant/full chart; sign comparison → two saved profiles → aspect evidence; and April 8, 2024 calendar → America/New_York → downloaded .ics with `DTSTART:20240408T182125Z`.

Additional browser checks cover the separate personal birth calendar, a date-only portrait, Chinese and Maya outputs, personal correspondences, 18px default reference paragraphs and larger reading mode, no root horizontal overflow in tested phone views, and a downloaded readable astral card. These flows produced zero runtime errors and zero external HTTP requests. `artifacts/browser-qa.json` records the scope; screenshots and sample downloads are saved alongside it. The test uses synthetic people, not private user birth details.

This is real Chromium testing with a phone viewport, not a physical-device test. Cloud policy blocks file URLs, so the exact standalone document was served unchanged over loopback HTTP for verification; file-origin launch/storage behavior on the user's Mac remains unobserved. Remote desktop tools were unavailable, so no claim of a hand-operated physical-phone check is made. Responsive layouts, keyboard controls, reduced-motion support, semantic tables, and input labels are implemented.

## Intentional calculation limits

- Additional Jyotish divisions beyond D1/D9, BaZi luck pillars/apparent solar time, Chiron, lots, and astrocartography remain reference-only with explicit calculator availability labels. Solar/lunar longitude returns and secondary progressed planetary positions are now interactive; return houses and progressed angles remain unavailable.
- Composite planets are shorter-arc midpoints; composite angles and houses are omitted.
- Mean node positions are approximate, not true nodes. Retrograde station times use a centered one-day rate and are approximate.
- Unknown-time profiles with a known place use labeled local-noon samples for degrees/aspects, flag alternative signs across the local day, and omit houses/angles/rulers. Date-only profiles without a birthplace cover UTC−12 to UTC+14, show sign alternatives, and omit precise degree/aspect/retrograde and angle/house/ruler claims. They are excluded from synastry and exact-time tools.
- Local civil times before 1970 require confirmation against historical records. Supported birth dates are 1900–2099 and latitudes 66° S–66° N.
- Personal transits are a 1°-orb snapshot at local noon, rather than exact transit searches.
- Eclipse local visibility is unavailable. Moonrise/set are coordinate-based geometric horizon estimates without terrain or weather.


## V2 return validation

The new longitude-return solver is compared with Swiss Ephemeris 2.10.3 `solcross_ut` and `mooncross_ut`, using independently calculated natal longitudes, Moshier apparent geocentric tropical positions, and the same UTC search start. The four fixtures are retained in `tests/reference-returns.json`.

| Birth fixture | Return | Absolute difference from Swiss Ephemeris |
| --- | --- | ---: |
| Greenwich, 2000-01-01 12:00 UTC | Solar | 18.106 seconds |
| Greenwich, 2000-01-01 12:00 UTC | Lunar | 3.388 seconds |
| London, 1995-11-07 14:30 UTC | Solar | 23.717 seconds |
| London, 1995-11-07 14:30 UTC | Lunar | 6.315 seconds |

Regression tolerance is 90 seconds in these samples. Every result also checks the solver residual against its own natal longitude to within 0.000001°. A return is the first crossing on or after the selected date; it need not fall in that Gregorian year when the cycle's crossing is already past the start date.

Secondary progressions use the explicitly documented mapping of one ephemeris day to one elapsed tropical year (365.2422 civil days). The test checks the resulting ephemeris instant exactly at a constructed twenty-year interval and verifies that no progressed houses are assigned. Their planetary positions use the same independently checked ephemeris as natal charts; no claim of independently validated progressed angles is made.

V2 replaces the small text with comfortable reading sizes and a locally saved scale control, opens reference entries in a wide reader, and expands both content and interaction. V3 adds actual Chromium desktop and phone-viewport checks as described above; no physical phone was observed.


## V3 birth date and calendar validation

- Maya conversion: seven dates spanning 1900–2099, including leap day and December 21, 2012, are compared with the independent public-domain Fourmilab Calendar Converter. The app uses GMT 584283 and reproduces 13.0.0.0.0 / 4 Ajaw / 3 Kankin on the 2012 anchor. Fixtures and reference URL are in `tests/reference-maya.json`.
- Chinese conversion: Lunar New Year boundaries are checked for 1982 (January 24 Rooster → January 25 Dog) and 2024 (February 9 Rabbit → February 10 Dragon). The 1982 Hong Kong Observatory Gregorian/lunar table confirms Ren-xu (Water Dog), and December 16 = lunar month 11, day 2. March 22, 2023 checks leap month 2, day 1. Sources: https://www.hko.gov.hk/en/gts/time/conversion.htm and https://www.hko.gov.hk/en/gts/time/calendar/pdf/files/1982e.pdf. Conversion uses the runtime's ICU calendar; the browser was tested as well as Node. These sample checks are not exhaustive validation of every date or ICU version.
- Date-only December 16, 1982 returns Sagittarius Sun and Sagittarius/Capricorn Moon possibilities across the conservative cross-zone window, with no Ascendant or houses invented. Names do not affect astronomical positions.
- Correspondences follow calculated/possible placements; optional full-planet coverage is checked. Modern month stones remain a separate list, historical metal associations are labeled, and colors are identified as the Atlas editorial palette.
- Birth calendar checks include leap-day omission, matching Chinese leap status, omission of events before birth, exact known-time solar/lunar returns, and omission of those exact returns without a birth moment. Filtered .ics exports preserve all-day civil dates and UTC exact moments; Unicode line folding respects the 75-byte limit.
- Interactions cover any-date creation, saving several people, reloading and upgrading a date-only portrait, Moon/rising/ruler details, tradition tabs, materials, calendar switching/filtering/exports, full-card/JSON downloads, backup import, and offline city selection (Bogotá, America/Bogota). The original four end-to-end flows remain covered.
- Personal card HTML escapes user-entered names. Standalone app bundles all required code, fonts, and the local GeoNames index. No health or universal predictive claims are introduced by the calendar results or symbolic materials.


## V4 Personal Companion validation

`tests/personal-tools.test.ts` adds 31 passing results to the existing 64. Fixtures in `tests/reference-personal-swiss.json` come from independently installed Swiss Ephemeris 2.10.3 Moshier calculations, and `tests/reference-pillars.json` from lunar-javascript 1.7.8 (MIT). Neither reference library is a runtime dependency or included in the standalone bundle. The optional Swiss generation script is `scripts/independent-personal-reference.py`.

Sidereal checks cover Lahiri and Fagan–Bradley at 1900-01-01, 1950-06-01, 2000-01-01, 2024-04-08, and 2099-12-31 with matching geocentric positions, effective ayanamsa/nutation conventions, UTC, and Greenwich observer. Mean ayanamsa agrees within 0.000001° in these samples. Maximum planetary difference is below 0.02°; Ascendant below 0.002°. The largest planetary difference is the far-future Moon sample, reflecting model differences including future time scales. These are sample tolerances, not guarantees for every birth moment; classification near a boundary is sensitive to settings. Nakshatra and pada agree for the checked Moon samples. D9 mapping, dasha balance/sequence, continuous major periods, and proportional subperiods are checked separately under the documented 365.25-day-year convention; dasha timing is a traditional calculation, not a forecast validation.

Exact personal transit peaks are independently compared for Mars square natal Sun, Venus trine natal Moon, and Saturn sextile natal Sun during 2024, using the Greenwich 2000 natal fixture. Each agrees within the two-hour regression tolerance using separately calculated natal targets. The solver's own angular residual is below 0.000001°, and both orb edges satisfy the selected threshold. An orb window is a continuous interval of angular proximity, not a measured duration of influence. Separate retrograde passes can share an orb window. The UI lists peaks within the requested search horizon and explains that an active contact may peak outside it.

Ten Four Pillars cases match the independent calendar library with China standard civil-clock rules, including just before/after Li Chun on February 4, 2024, a 1984 year boundary, ordinary day/month examples, and midnight. Additional tests check both explicit 23:00 and midnight day/hour rollover variants. Year/month use physical apparent solar longitude; day/hour use the selected civil clock. Apparent solar time, hidden-stem strength weighting, and luck pillars remain unavailable. Near a solar-term boundary, small model or recorded-time differences can change a pillar.

Other checks cover unknown-time rejection for exact tools, DST-gap handling in sampled time ranges, inclusion of both range endpoints, principal phases and global eclipse events, selected station presence, all-day versus UTC exports, one standard VALARM per exported planner event, twelve printable months, HTML escaping, supporting chart evidence, source-labeled correspondence records, and creator credit.

`scripts/personal-browser-qa.mjs` tests all eight tools in real headless Chromium, plus persistence, full backup/export, fresh-context mobile import, and delete controls. It checks the 390px phone layout for every tool and at least 18px paragraph text. A downloaded annual planner was opened in Chromium and rendered to PDF; calendar downloads contain actual standard alarm blocks. Original four browser flows were rerun against V4 as well. Both browser reports show zero runtime errors and zero external HTTP requests in the tested flows. Reports are `artifacts/browser-qa.json` and `artifacts/personal-browser-qa.json`; screenshots and synthetic sample downloads are generated alongside them.

Browser scope remains desktop/phone viewport emulation over loopback HTTP, not a physical phone or a file-origin session on the user's Mac. Cloud policy blocks file URLs. Calendar alarm delivery depends on importing the .ics into a calendar application and that application's alarm settings; the app has no background notification service.


## V4.1 guide, personality, and runes

Twelve new automated results bring the full suite to 107. They verify complete 24-rune references, distinct sampling without replacement, invalid journal-record rejection, all twelve signs’ visible positive/challenging traits, direct and saved personality readings, date-only ambiguity handling, guide task navigation, rune favorites, saved-note updates, full export/import merge, and deletion. The guide’s glossary explicitly explains monthly lunar returns. A new locally bundled OFL runic font ensures consistent glyph display.

`scripts/guide-browser-qa.mjs` passes in desktop 1440×1000 and phone 390×844 Chromium, with no page runtime errors or external HTTP requests. It exercises the guide, sign profiles and search, the My Personality deep link, saved exact chart and arbitrary-date readings, placement jump buttons, all 24 rune buttons, historical uncertainty, draws, notes, favorites, backup/import and individual deletion. Phone checks cover the largest type setting, no root horizontal overflow, font loading, and accessible paragraph sizes. Synthetic profiles and notes are used. `ATLAS_LIVE_URL` runs the same checks against the deployed production origin. The existing browser suites cover the original app and eight Personal Companion tools.

Historical rune context is sourced separately from modern editorial reflection. The names/glosses are reconstructed or informed by later traditions; uncertain readings are identified. No runic personality claims are derived from a birthday. Random draws are reflective prompts rather than verified predictions. These content conventions do not validate divination.
