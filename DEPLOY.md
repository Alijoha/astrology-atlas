# Publish Astrology Atlas on Vercel

This repository is a Vite + React static application. No API keys, environment variables, database, or paid add-ons are required for the current app.

1. In Vercel, choose Add New → Project and import the GitHub repository `Alijoha/astrology-atlas`.
2. If prompted, give the Vercel GitHub integration access to this repository.
3. Use the defaults from vercel.json: Vite, root directory `.`, install `npm ci`, build `npm run build`, output `dist`, Node.js 22.x.
4. Select Deploy. Your public site will get a vercel.app address. The source repository can stay private.
5. Later pushes to main will deploy automatically when the Git integration is connected. Manage custom domains in the Vercel project settings.

The app uses hash routes, so reference links open directly without a server router. City data and fonts are bundled local assets. Third-party license notices are available at /THIRD_PARTY_NOTICES.txt.

Saved charts, journals, milestones, favorites, and collections stay in each visitor's browser. The production origin has separate storage from localhost or the downloaded HTML file: use Settings → Export in the old app, then Settings → Import file on the live site. A later domain change also creates a separate storage origin.

To validate locally: `npm ci`, `npm test`, `npm run build`, `npm run preview`.

Created by Johanna Polanco with love ♡ · US Army veteran.
