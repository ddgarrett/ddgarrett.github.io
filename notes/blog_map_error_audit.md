# Garrett Blog & Map Error Audit

Full audit of live blog HTML at [garrettblog.com](https://www.garrettblog.com) cross-referenced against photo map files in this repository.

## Executive summary

| Category | Count |
|---|---|
| Unique map photo URLs checked | 1599 |
| Map captions matching blog figcaption | 541 |
| Map URLs not found in blog HTML | 973 |
| Blog `p id` ≠ following image (HTML bug) | 7 |
| Blog figures missing `<figcaption>` | 4 |
| Malformed prose links in blog HTML | 0 |
| Map caption errors tied to `p id` mismatch | 4 |
| Map caption errors tied to missing figcaption | 2 |
| Map captions using filename instead of title | 3 |
| Map caption accent/Unicode differences | 0 |
| Map caption minor wording differences | 28 |
| Other substantive map caption mismatches | 48 |
| Fixed in this repo | 1 |

---

## 1. Blog HTML structural errors

These exist in the published blog source HTML. They can break `#fragment` links and confuse automated caption extraction.

### 1.1 `p id` anchor does not match the following image

When the paragraph anchor filename differs from the image filename in the next `<figure>`, map links using the `p id` as the `#fragment` may point at the wrong photo or caption.

| Month | `p id` fragment | Actual image | Blog figcaption |
|---|---|---|---|
| `2022/04` | `PXL_20220425_140113434.jpg` | `PXL_20220425_144302230.jpg` | Syverkiosken Hotdog Stand |
| `2023/04` | `PXL_20230422_001945936.jpg` | `PXL_20230422_001953785.jpg` | Shore Near Jodogahama Beach |
| `2023/04` | `PXL_20230421_043134673.jpg` | `PXL_20230421_044644561.jpg` | Hitachi Seaside Park |
| `2023/04` | `PXL_20230420_063053296.jpg` | `PXL_20230420_082515301.jpg` | Sailing Under Yokohama Bridge |
| `2023/04` | `PXL_20230419_011526744.jpg` | `PXL_20230417_210042230.jpg` | Fish Auction |
| `2023/05` | `2023-04_japan_trip_map` | `2023-04_Japan_Map.png` | Japan Trip Map |
| `2023/05` | `PXL_20230503_070944760.jpg` | `PXL_20230503_071041809.jpg` | Kyoto Imperial Palace |

### 1.2 Figures missing `<figcaption>`

| Month | Image | URL |
|---|---|---|
| `2023/10` | `PXL_20231010_200315425.jpg` | `https://www.garrettblog.com/2023/10#PXL_20231010_200315425.jpg` |
| `2023/10` | `PXL_20231010_200951478.jpg` | `https://www.garrettblog.com/2023/10#PXL_20231010_200951478.jpg` |
| `2023/10` | `PXL_20231010_201258258.jpg` | `https://www.garrettblog.com/2023/10#PXL_20231010_201258258.jpg` |
| `2023/10` | `IMG_3507.JPG` | `https://www.garrettblog.com/2023/10#IMG_3507.JPG` |

### 1.3 Malformed prose links

*(none currently)*

**Note:** An earlier audit found a broken link on `2023/10` (`href="[https://tongatourguide.com/..."` with a stray `[`). That link has since been corrected on the live blog to a valid `https://tongatourguide.com/...` URL.

---

## 2. Map caption errors caused by blog HTML bugs

### 2.1 Caused by `p id` ≠ image mismatch

| URL | Map caption | Blog figcaption | Map file(s) |
|---|---|---|---|
| `https://www.garrettblog.com/2022/04#PXL_20220425_140113434.jpg` | 04/25/2022 - Godt Brd Grnerlkka Brown Cheese and Smoked Salmon | Syverkiosken Hotdog Stand | `2022-04_europe_trip.html` |
| `https://www.garrettblog.com/2023/04#PXL_20230419_011526744.jpg` | 04/19/2023 - Imperial Palace | Fish Auction | `2023-04_japan_trip.html` |
| `https://www.garrettblog.com/2023/04#PXL_20230420_063053296.jpg` | 04/20/2023 - Yokohama Cruise 1 | Sailing Under Yokohama Bridge | `2023-04_japan_trip.html` |
| `https://www.garrettblog.com/2023/04#PXL_20230422_001945936.jpg` | 04/22/2023 - Miyako Jodogahama | Shore Near Jodogahama Beach | `2023-04_japan_trip.html` |

### 2.2 Caused by missing blog figcaption

| URL | Map caption | Blog figcaption | Map file(s) |
|---|---|---|---|
| `https://www.garrettblog.com/2023/10#PXL_20231010_200951478.jpg` | 10/10/2023 - N Pali Coast | (missing figcaption) | `2023-10-south_pacific_cruise.html` |
| `https://www.garrettblog.com/2023/10#PXL_20231010_201258258.jpg` | 10/10/2023 - N Pali Coast | (missing figcaption) | `2023-10-south_pacific_cruise.html` |

---

## 3. Other map caption mismatches

### 3.1 Filename used as map caption

| URL | Map caption | Blog figcaption |
|---|---|---|
| `https://www.garrettblog.com/2023/04#PXL_20230422_001953785.jpg` | 04/22/2023 - PXL_20230422_001953785.jpg | Shore Near Jodogahama Beach |
| `https://www.garrettblog.com/2024/01#PXL_20240128_181339402.jpg` | 01/28/2024 - PXL_20240128_181339402.jpg | El Paraiso Sign |
| `https://www.garrettblog.com/2024/01#PXL_20240128_201537076.jpg` | 01/28/2024 - PXL_20240128_201537076.jpg | Manzanillo |

### 3.2 Accent or Unicode character differences

*(none)*

### 3.3 Minor wording differences

| URL | Map caption | Blog figcaption |
|---|---|---|
| `https://www.garrettblog.com/2023/04#PXL_20230424_034637510.jpg` | 04/24/2023 - Lake Tazawa | Tatsuko Statue at Lake Tazawa |
| `https://www.garrettblog.com/2023/04#PXL_20230426_024630331.jpg` | 04/26/2023 - Haedong Yonggungsa Temple | View of Haedong Yonggungsa Temple |
| `https://www.garrettblog.com/2023/04#PXL_20230427_012835559.jpg` | 04/27/2023 - Peace Park | Peace Park Statue |
| `https://www.garrettblog.com/2023/05#PXL_20230501_105029086.NIGHT.jpg` | 05/01/2023 - View During Evening Tour | Night View During Evening Tour |
| `https://www.garrettblog.com/2023/05#PXL_20230501_223845174.jpg` | 05/02/2023 -  Kiyomizu-dera | Entrance to Kiyomizu-dera |
| `https://www.garrettblog.com/2023/05#PXL_20230505_043658490.jpg` | 05/05/2023 - Osaka Aquarium | Osaka Aquarium Puffin |
| `https://www.garrettblog.com/2023/05#PXL_20230505_100040053.jpg` | 05/05/2023 - Umeda Sky Building | View From Umeda Sky Building |
| `https://www.garrettblog.com/2023/05#PXL_20230509_031201220.jpg` | 05/09/2023 - Mt. Inasayama Observatory | View From Mt. Inasayama Observatory |
| `https://www.garrettblog.com/2023/05#PXL_20230515_003534466.jpg` | 05/15/2023 - Katsuren Castle Ruins | View From Katsuren Castle Ruins |
| `https://www.garrettblog.com/2023/05#PXL_20230516_012419273.jpg` | 05/16/2023 - Tamatorizaki Observation Platform | View From Tamatorizaki Observation Platform |
| `https://www.garrettblog.com/2023/05#PXL_20230516_023954322.jpg` | 05/16/2023 - Yoneko Yaki Kobo Shisa Farm | Yoneko Yaki Kobo Shisa Farm Craft Store |
| `https://www.garrettblog.com/2023/07#PXL_20230722_204713276.jpg` | 07/22/2023 - Boston | Harpoon Brewery - Boston |
| `https://www.garrettblog.com/2023/07#PXL_20230724_234215038.jpg` | 07/24/2023 - At Sea | Sunset At Sea |
| `https://www.garrettblog.com/2023/07#PXL_20230731_142758286.jpg` | 12:27pm - Glacier | Prince Christian Sound Glacier |
| `https://www.garrettblog.com/2023/08#PXL_20230802_104525644.jpg` | 08/02/2023 - Dokkan Brugghús Ísafjörður Iceland | Dokkan Brugghús |
| `https://www.garrettblog.com/2023/08#PXL_20230802_150730356.jpg` | 08/02/2023 - Vigur Island Iceland | Vigur Island |
| `https://www.garrettblog.com/2023/08#PXL_20230804_085708334.PANO.jpg` | 08/04/2023 - Goðafoss Falls Iceland | Goðafoss Falls |
| `https://www.garrettblog.com/2023/08#PXL_20230804_103100442.jpg` | 08/04/2023 - Skútustaðagígar and Lake Mývatn Iceland | Skútustaðagígar and Lake Mývatn |
| `https://www.garrettblog.com/2023/08#PXL_20230804_131250742.PANO.jpg` | 08/04/2023 - Myvatn Geothermal Area Iceland | Myvatn Geothermal Area |
| `https://www.garrettblog.com/2023/08#PXL_20230806_110742093.jpg` | 08/06/2023 - Fort Charlotte | Fort Charlotte Cannon - Aimed At Cruise Ship |
| `https://www.garrettblog.com/2023/08#PXL_20230806_120938032.jpg` | 08/06/2023 - Shetland Museum & Archives | Outside The Shetland Museum & Archives |
| `https://www.garrettblog.com/2023/08#PXL_20230807_051309856.jpg` | 08/07/2023 - At Sea | At Sea Sunrise |
| `https://www.garrettblog.com/2023/08#PXL_20230808_091736435.jpg` | 08/08/2023 - Cube House | Cube Houses |
| `https://www.garrettblog.com/2023/08#PXL_20230812_120823933.jpg` | 08/12/2023 - Lews Castle - Stornoway Scotland | Lews Castle |
| `https://www.garrettblog.com/2023/08#PXL_20230815_135633837.jpg` | 08/15/2023 - The Blue Lagoon | Blue Lagoon |
| `https://www.garrettblog.com/2023/08#PXL_20230818_190023701.jpg` | 08/18/2023 - 5:00 pm Aappilattoq Village | Aappilattoq Village |
| `https://www.garrettblog.com/2023/08#PXL_20230820_081958790.jpg` | 08/20/2023 - At Sea | Sunrise At Sea |
| `https://www.garrettblog.com/2025/10#PXL_20251001_181129711.NIGHT.jpg` | 10/01/2025 - Native American Underground Structure | Native American Underground Structure - Blanding UT |

### 3.4 Other substantive mismatches

| URL | Map caption | Blog figcaption |
|---|---|---|
| `https://www.garrettblog.com/2022/05#PXL_20220507_112146001.jpg` | 05/07/2022 - Monument  Don Quichotte | Monument à Don Quichotte |
| `https://www.garrettblog.com/2023/02#PXL_20230204_173639411.jpg` | 02/04/2023 -  Parroquia de Nuestra Seora de Guadalupe Church | Parroquia de Nuestra Señora de Guadalupe Church |
| `https://www.garrettblog.com/2023/02#PXL_20230204_181708009.jpg` | 02/04/2023 - Bette Davis Mural | Betty Davis Mural |
| `https://www.garrettblog.com/2023/02#PXL_20230205_155547261.jpg` | 02/05/2023 - Cathedral Baslica Menor de Colima | Cathedral Basílica Menor de Colima |
| `https://www.garrettblog.com/2023/02#PXL_20230205_160421681.jpg` | 02/05/2023 - Jardn Libertad (Freedom Garden) | Jardín Libertad (Freedom Garden) |
| `https://www.garrettblog.com/2023/02#PXL_20230206_191047443.jpg` | 02/06/2023 - Plaza Repblica | Plaza República |
| `https://www.garrettblog.com/2023/02#PXL_20230216_232910545.jpg` | 02/16/2023 - Nuuanu Pali Lookout | Nuʻuanu Pali Lookout |
| `https://www.garrettblog.com/2023/04#PXL_20230423_003800892.jpg` | 04/23/2023 - Nebuta Museum | Aomori Nebuta Festival Float |
| `https://www.garrettblog.com/2023/04#PXL_20230425_232158805.jpg` | 04/26/2023 -Hwangryeong Mountain Observation Deck | View from Hwangryeong Mountain Observation Area |
| `https://www.garrettblog.com/2023/05#PXL_20230506_204142447.jpg` | 05/07/2023 - Leaving Yokahama - Cruise 2 | Princess Cruise Ship Coming Into Port |
| `https://www.garrettblog.com/2023/05#PXL_20230516_032236822.jpg` | 05/16/2023 - Kabira Bay View | View of Kabira Bay |
| `https://www.garrettblog.com/2023/05#PXL_20230516_055504003.jpg` | 05/16/2023 - Emerald Sea Observation Deck | View From Emerald Sea Observatory Deck |
| `https://www.garrettblog.com/2023/05#PXL_20230517_030534060.jpg` | 05/17/2023 - Nation Revolutionary Martyrs Shrine | National Revolutionary Martyrs' Shrine - Changing of the Guard |
| `https://www.garrettblog.com/2023/07#PXL_20230723_170026500.jpg` | 07/23/2023 - Bar Harbor Maine | Elizabeth "Fixing" a Tipped Boulder |
| `https://www.garrettblog.com/2023/07#PXL_20230725_133243002.jpg` | 07/25/2023 - Baddeck NS | Alexander Graham Bell Hydrofoil Prototype |
| `https://www.garrettblog.com/2023/07#PXL_20230725_170540885.jpg` | 07/25/2023 - Sydney Nova Scotia | World's Largest Fiddle |
| `https://www.garrettblog.com/2023/07#PXL_20230726_115230038.jpg` | 07/26/2023 - Steady Brook Newfoundland | Newfoundland and Labrador Heritage Tree |
| `https://www.garrettblog.com/2023/07#PXL_20230726_123709568.jpg` | 07/26/2023 - Corner Brook Newfoundland | View From Captain Cook Historic Site |
| `https://www.garrettblog.com/2023/07#PXL_20230729_124923497.jpg` | 07/29/2023 - Paamiut Greenland | Colorful Paamiut Buildings |
| `https://www.garrettblog.com/2023/07#PXL_20230730_150957159.jpg` | 07/30/2023 - Nanortalik Greenland | View From Nanortalik Outdoor Museum Tower |
| `https://www.garrettblog.com/2023/07#PXL_20230731_102054907.jpg` | 8:31am - Heading to Prince Christian Sound | Iceberg Near Entrance to Prince Christian Sound |
| `https://www.garrettblog.com/2023/08#PXL_20230802_065623249.jpg` | 08/02/2023 - Ísafjörður Iceland | Tugboat Escort |
| `https://www.garrettblog.com/2023/08#PXL_20230804_060245903.jpg` | 08/04/2023 - Akureyri Iceland | Water From Foss Steam Baths |
| `https://www.garrettblog.com/2023/08#PXL_20230804_121228867.jpg` | 08/04/2023 -  Dimmuborgir Lava Fields Iceland | Troll Turned Into Stone By Morning Light |
| `https://www.garrettblog.com/2023/08#PXL_20230806_074539473.NIGHT.jpg` | 08/06/2023 - Lerwick Scotland - Port View | Looking Back Towards Cruise Ship |
| `https://www.garrettblog.com/2023/08#PXL_20230808_074721057.jpg` | 08/08/2023 - Rotterdam Street Art | Street Art Example |
| `https://www.garrettblog.com/2023/08#PXL_20230810_075836565.jpg` | 08/10/2023 - Cork Port - Cobh | Cork (Cobh) Ireland Port |
| `https://www.garrettblog.com/2023/08#PXL_20230811_105322275.jpg` | 08/11/2023 - Giants Causeway | Giant's Causeway |
| `https://www.garrettblog.com/2023/08#PXL_20230814_111129685.jpg` | 08/14/2023 - Djúpivogur Tour | Our Ride |
| `https://www.garrettblog.com/2023/08#PXL_20230814_114312381.jpg` | 08/14/2023 - Final Waterfall on Tour | Unnamed Waterfall |
| `https://www.garrettblog.com/2023/08#PXL_20230815_104006081.jpg` | 08/15/2023 - Reykjavik Harbor Day 1 | Reykjavik From Our Ship |
| `https://www.garrettblog.com/2023/08#PXL_20230816_052055574.jpg` | 08/16/2023 - Reykjavik Day 2 | Reykjavik From Our Ship Day Two |
| `https://www.garrettblog.com/2023/08#PXL_20230816_104556568.PORTRAIT.jpg` | 08/16/2023 - Friðheimar Tomato Farm | Sunflowers at Friðheimar |
| `https://www.garrettblog.com/2023/08#PXL_20230818_144437808.jpg` | 08/18/2023 - 12:44 pm First Glacier | Prince Christian Sound Glacier |
| `https://www.garrettblog.com/2023/08#PXL_20230818_162507881.jpg` | 08/18/2023 -  2:25 pm Second Large Glacier | Prince Christian Sound Glacier |
| `https://www.garrettblog.com/2023/08#PXL_20230819_105300111.jpg` | 08/19/2023 - Saviors Church | Savior's Church |
| `https://www.garrettblog.com/2023/08#PXL_20230819_111155431.jpg` | 08/19/2023 - Lake View | Lake Overlook View |
| `https://www.garrettblog.com/2023/08#PXL_20230819_121134883.jpg` | 08/19/2023 - Rock and Man Carvings | One of 24 Rock and Man Art Carvings |
| `https://www.garrettblog.com/2023/08#PXL_20230821_121353180.jpg` | 08/21/2023 - Dare Devil Trail Viewpoint | View from Top of Dare Devil Trail |
| `https://www.garrettblog.com/2023/08#PXL_20230821_131728385.jpg` | 08/21/2023 - Fishing Point Emporium | Being Chased by a Polar Bear |
| `https://www.garrettblog.com/2023/08#PXL_20230822_123705124.jpg` | 08/22/2023 - St. Johns Welcoming Party | St. John's Welcoming Party |
| `https://www.garrettblog.com/2023/08#PXL_20230824_105354415.jpg` | 08/24/2023 - Halifax Port | Passenger Shadows As We Pull Into Port |
| `https://www.garrettblog.com/2023/08#PXL_20230824_142857677.jpg` | 08/24/2023 - Peggys Cove | Peggy's Cove Lighthouse |
| `https://www.garrettblog.com/2023/10#PXL_20231008_234639856.jpg` | 10/08/2023 - Liliuokalani Gardens | Liliʻuokalani Gardens |
| `https://www.garrettblog.com/2023/10#PXL_20231010_022849483.jpg` | 10/09/2023 - N Pali Coast | Nā Pali Coast |
| `https://www.garrettblog.com/2024/12#PXL_20241207_023129677.jpg` | 12/07/2024 - View From Hike Leading to \nKayangan Lake | View From Hike Leading to Kayangan Lake |
| `https://www.garrettblog.com/2026/05#PXL_20260427_034447861.jpg` | 04/27/2026 - View from Airbnb Balcony | View from BGC Airbnb Balcony |
| `https://www.garrettblog.com/2026/05#PXL_20260505_034225488.jpg` | 05/05/2026 - Float Cottage Being Towed | Floating Cottage Being Towed |

---

## 4. Map URLs not found in blog HTML

These map links point to a `#fragment` that does not appear anywhere in that month's live blog HTML. They may be stale, typo'd, or reference photos not yet published to that month archive.

**Primary source:** Almost all of these come from `2023-04_japan_trip-initial_map.html`, an early Japan trip map containing ~1,000+ photo URLs that were never published to the corresponding blog month pages (or use filenames that do not exist in the blog HTML). A smaller number come from `2024-02-14_valentines_day_map.html` (cross-trip references) and `2024-11_asia_trip.html` (1 URL).

| Map file | Unverified URL count |
|---|---:|
| `2023-04_japan_trip-initial_map.html` | ~968 |
| `2024-02-14_valentines_day_map.html` | ~23 |
| `2024-11_asia_trip.html` | 1 |

The canonical Japan trip map `2023-04_japan_trip.html` does **not** contribute to this list — its 32 URLs all exist on the live blog.

| URL | Map caption |
|---|---|
| `https://www.garrettblog.com/2023/04#PXL_20230417_205439029.jpg` | 04/18/2023 - PXL_20230417_205439029.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_205620206.jpg` | 04/18/2023 - PXL_20230417_205620206.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_205658024.jpg` | 04/18/2023 - PXL_20230417_205658024.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_205732176.jpg` | 04/18/2023 - PXL_20230417_205732176.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_212907661.jpg` | 04/18/2023 - PXL_20230417_212907661.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_213300414.jpg` | 04/18/2023 - PXL_20230417_213300414.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_220305688.jpg` | 04/18/2023 - PXL_20230417_220305688.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_220819003.jpg` | 04/18/2023 - PXL_20230417_220819003.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_222339098.jpg` | 04/18/2023 - PXL_20230417_222339098.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_222423582.jpg` | 04/18/2023 - PXL_20230417_222423582.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_222614308.jpg` | 04/18/2023 - PXL_20230417_222614308.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_222813508.jpg` | 04/18/2023 - PXL_20230417_222813508.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_223024768.jpg` | 04/18/2023 - PXL_20230417_223024768.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_224803809.jpg` | 04/18/2023 - PXL_20230417_224803809.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_224911008.jpg` | 04/18/2023 - PXL_20230417_224911008.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_225121588.PANO.jpg` | 04/18/2023 - PXL_20230417_225121588.PANO.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_225535188.jpg` | 04/18/2023 - PXL_20230417_225535188.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_225737797.jpg` | 04/18/2023 - PXL_20230417_225737797.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230417_230024770.jpg` | 04/18/2023 - PXL_20230417_230024770.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_040740945.jpg` | 04/18/2023 - PXL_20230418_040740945.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_044105941.jpg` | 04/18/2023 - PXL_20230418_044105941.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_044347608.jpg` | 04/18/2023 - PXL_20230418_044347608.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_045251797.NIGHT.jpg` | 04/18/2023 - PXL_20230418_045251797.NIGHT.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_045405588.NIGHT.jpg` | 04/18/2023 - PXL_20230418_045405588.NIGHT.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_045558060.jpg` | 04/18/2023 - PXL_20230418_045558060.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_050325691.jpg` | 04/18/2023 - PXL_20230418_050325691.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_050405803.jpg` | 04/18/2023 - PXL_20230418_050405803.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_050658736.jpg` | 04/18/2023 - PXL_20230418_050658736.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_051152087.jpg` | 04/18/2023 - PXL_20230418_051152087.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_052253072.jpg` | 04/18/2023 - PXL_20230418_052253072.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_055404688.jpg` | 04/18/2023 - PXL_20230418_055404688.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_055516941.jpg` | 04/18/2023 - PXL_20230418_055516941.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_055729141.jpg` | 04/18/2023 - PXL_20230418_055729141.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_071337258.jpg` | 04/18/2023 - PXL_20230418_071337258.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_093608658.jpg` | 04/18/2023 - PXL_20230418_093608658.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_093946567.jpg` | 04/18/2023 - PXL_20230418_093946567.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_094101011.jpg` | 04/18/2023 - PXL_20230418_094101011.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_101418196.jpg` | 04/18/2023 - PXL_20230418_101418196.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_101631738.jpg` | 04/18/2023 - PXL_20230418_101631738.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_102022182.jpg` | 04/18/2023 - PXL_20230418_102022182.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_215414814.jpg` | 04/19/2023 - PXL_20230418_215414814.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230418_221127700.jpg` | 04/19/2023 - PXL_20230418_221127700.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_003134962.jpg` | 04/19/2023 - PXL_20230419_003134962.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_011543027.jpg` | 04/19/2023 - PXL_20230419_011543027.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_011640725.jpg` | 04/19/2023 - PXL_20230419_011640725.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_011917579.jpg` | 04/19/2023 - PXL_20230419_011917579.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_011945464.jpg` | 04/19/2023 - PXL_20230419_011945464.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_012425014.jpg` | 04/19/2023 - PXL_20230419_012425014.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_012544318.jpg` | 04/19/2023 - PXL_20230419_012544318.jpg |
| `https://www.garrettblog.com/2023/04#PXL_20230419_012800381.jpg` | 04/19/2023 - PXL_20230419_012800381.jpg |

*...and 923 more.*

---

## 5. Already corrected in this repository

| URL | Was | Now | Commit |
|---|---|---|---|
| `https://www.garrettblog.com/2023/10#PXL_20231020_183416062.jpg` | 10/20/2023 - The Princess and The Farmer | 10/20/2023 - Greeting at Port | `5849e37` |

The blog HTML always had the correct figcaption (`Greeting at Port`). The map had incorrectly used the next photo's caption.

---

## 6. Previously reported issue — now resolved on the blog

### `2026/01` empty month page

**Earlier finding:** `https://www.garrettblog.com/2026/01` had no photo post content while `2026-01_nz_au.html` linked 15 photos there.

**Current status:** The January 2026 blog post is now published. All 15 map `#fragment` anchors resolve on the live page.

---

## 7. Blog months with no structural HTML errors detected

`2022/05`, `2023/01`, `2023/02`, `2023/07`, `2023/08`, `2023/11`, `2024/01`, `2024/08`, `2024/09`, `2024/11`, `2024/12`, `2025/01`, `2025/02`, `2025/04`, `2025/06`, `2025/09`, `2025/10`, `2025/12`, `2026/01`, `2026/05`

---

## 8. Methodology

1. Fetched raw HTML for all 24 blog month URLs referenced by map files.
2. Parsed `post-body entry-content` for `<p id>`, `<figure>`, `<img>`, and `<figcaption>`.
3. Flagged structural HTML errors and malformed links.
4. Extracted captions from all source map HTML files (excluding `all_maps.html` and `2023_trips.html`).
5. Compared map link text to blog figcaptions; categorized differences by likely root cause.
