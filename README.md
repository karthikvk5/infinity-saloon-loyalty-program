# Infinity Saloon — six HTML emails

Open **index.html** to browse all six emails and switch between desktop and mobile previews.

## Included

| File | Design | Timing in Figma |
|---|---|---|
| 00-loyalty-introduction.html | Good cuts. Great rewards. | Program introduction |
| 01-after-haircut-1.html | One down. Five to go. | 15 days after haircut 1 |
| 02-after-haircut-2.html | Two down. Keep it going. | 15 days after haircut 2 |
| 03-after-haircut-3.html | Halfway to your rewards. | 15 days after haircut 3 |
| 04-after-haircut-4.html | Four down. Two to go. | 15 days after haircut 4 |
| 05-after-haircut-5.html | One more cut. Two rewards. | 15 days after haircut 5 |

These are the six designs present in the supplied Figma file: an introduction and five milestone follow-ups. There was no separate sixth-haircut redemption design.

Each email includes its own inline CSS and embedded responsive CSS. `responsive.css` is an editable reference copy; the emails do not depend on that separate file. Each `.txt` file is a plain-text alternative. `mailers.json` contains suggested subjects taken from the design headlines, preheaders, timing, and Figma node IDs. `assets/` contains shared images and fonts. `previews/` contains rendered desktop and mobile previews.

## Configured for CleverTap

- Main visit buttons and the footer WhatsApp contact link: https://wa.me/917676067811 (the supplied number, normalized without the plus sign).
- Google Maps and the review badge: https://maps.app.goo.gl/jvKjBARguMMVW9qH8
- Postal address: Vijaya Bank Layout Bangalore
- Unsubscribe link: `*|UNSUBSCRIBE|*`, CleverTap's documented replacement tag.
- The previous Facebook, Instagram and X links were replaced with one clearly labeled WhatsApp button because only a WhatsApp destination was supplied.

## Before sending

1. Upload the contents of `assets/` to a public HTTPS asset folder or your email platform's image library. Replace the relative image and font paths in the HTML with their public URLs. Images currently work in the local preview only.
2. Import each HTML file using CleverTap's custom HTML email editor. Subjects and preheaders are in `mailers.json`; each matching `.txt` file is the plain-text alternative.
3. Confirm your CleverTap email channel has its unsubscribe destination configured. The `*|UNSUBSCRIBE|*` tag is resolved during sending and does not work as a normal local-preview link. For Amazon SES/custom SMTP, follow CleverTap's unsubscribe-page setup instructions below.
4. Test the campaign through CleverTap to verify images, links and inbox layout. Configure the journey timing separately: introduction plus follow-ups 15 days after each of haircuts 1–5. No campaigns have been created or sent.

Optional asset-path helper: copy `config.example.json` to `config.json`, set `asset_base_url`, then run `python prepare-for-send.py config.json`. This creates `ready-to-import/` with public asset URLs, preserving all configured links and the CleverTap unsubscribe tag. For platforms that rename uploads, update each image URL directly instead.

Official CleverTap reference: https://docs.clevertap.com/docs/handling-unsubscribes

## Design and compatibility notes

- Live HTML text, table-based layout, 720px desktop width, mobile stacking, explicit image sizes, alt text, and Outlook width/font fallbacks.
- Original red (#f40606), charcoal (#20201e), yellow wordmark, copy, photos, and milestone progression preserved. The source's small gray text on red has limited contrast and was retained to match the supplied design.
- Photo crops, circular logo and milestone stamps come from Figma exports; vector icons were converted to PNG for email use. No complete email is flattened into an image.
- Inter is included for local previews and clients that support web fonts; Arial/Helvetica are fallbacks. Some email clients may alter fonts, colors, spacing, or decorative rounding.
- Browser checks cover all six at 720px, 375px, and 320px. These are not screenshots from Gmail, Outlook, or Apple Mail; actual inbox rendering remains to be tested through your sending platform.
- The 4.9 / 1.3k reviews claim is copied from the supplied artwork and has not been independently verified.

Source: https://www.figma.com/design/6sVgfqTA47whCmMo5dbQb6/Infinity-Saloon-Newsletter
