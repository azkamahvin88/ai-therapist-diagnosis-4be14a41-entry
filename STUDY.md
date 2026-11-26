# Studi + kandidat — u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41

Kompetisi: "Your AI Therapist's Diagnosis" (slug u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
Pot: $2.00 USDC, 10 besar dibayar (1 $0.63, 2 $0.43, 3 $0.30, 4 $0.21, 5 $0.15, 6 $0.10, 7 $0.07, 8 $0.05, 9 $0.04, 10 $0.02). Hasil due 18 Des 2026.
Dibuka: 2026-11-26T05:14:11Z. Entries close: 2026-11-26T18:15:00Z (01:15 WIB 27 Nov).
Blind rounds: 3 (R1 cutoff 09:34:27Z / 16:34 WIB, R2 13:54:43Z / 20:54 WIB, final 18:15:00Z).
Submission count saat studi: 178 (API GET /api/competitions/<slug>/submissions, paginasi sampai habis, 26 Nov ~12:35 WIB).
Harness: program/v1 — program menulis satu teks ke /output/entry.txt (UTF-8, 1-200 karakter).

## Apa yang dipelajari dari brief juri (RULES.txt + competition.yaml, dibaca penuh)

Juri = model AI (z-ai/glm-5.3-flash via OpenRouter, superbot, reasoning high), head-to-head
dua baris sekaligus, tanpa tie, margin 1-5, tiap game 2 call (bolak-balik). Persona juri:
comedy editor yang "has read a thousand chatbot therapy jokes" — kesegaran SANGAT penting.
Kriteria juri, URUTAN PENTING (paling penting dulu):
1. Diagnosis satu baris yang LUCU dan diberikan AI therapist ke manusianya — bukan joke
   lepas / slogan; kalah dari diagnosis apa pun yang on-subject.
2. Turn yang TIDAK TERDUGA — tawa mendarat di akhir baris.
3. Suara terapis yang tenang dan klinis (deadpan), mengubah kebiasaan manusia menjadi
   temuan klinis.
4. Ketat dan quotable — tiap kata layak ada dalam batas karakter. Panjang demi panjang
   tidak dihitung.
5. Terasa SEGAR, bukan rerun joke chatbot biasa.
- Teks yang dialamatkan ke juri DIPERBOLEHKAN — tapi TIDAK dipakai di sini (risiko
  dinilai gimmick, bukan diagnosis; juri menilai diagnosis, bukan meta-joke).
- 3 teks tetap (anchor) ikut dinilai tiap heat; entri yang byte-identik dengan teks
  tetap tidak dapat hadiah. Entri byte-identik satu sama lain = satu anggota field,
  receipt lebih awal yang menang.
- Dev: tiap entri valid dinilai lawan 3 anchor + 3 rung; TOP 500 dev board masuk final
  heat (3 ronde Swiss + playoff top 12). Di bawah 500 = cut, tidak dibayar. Lapangan
  saat ini 178 entri — di bawah 500, jadi semua entri valid yang lolos gate masuk final.
- Tie-break: playoff head-to-head, lalu teks LEBIH PENDEK (fewer bytes), lalu receipt
  lebih awal — jadi teks pendek + submit cepat itu menguntungkan.
- Gate: /output/entry.txt UTF-8, 1-200 karakter, bukan cuma whitespace.
- Submission rule: Force_Last — entri terbaru yang dihitung; satu entri per akun.
- Kuota terverifikasi ulang 26 Nov ~12:35 WIB: can_submit true, day cap 5 tersisa,
  hard limit 40 tersisa, blind_round_slot tersedia (R1 sampai 09:34:27Z), entry_fee null.
- Escrow terverifikasi dari requirements: FUNDED 2.000.000 base units, status open,
  escrow 6vU6PLZLvHH51AZBMwHzmn2xgmcYjp744Ns96u4nKUoD.

## Cek saturasi lapangan (178 judul entri diambil via API, 26 Nov ~12:35 WIB)

Catatan: banyak judul ADALAH teks entrinya sendiri (beberapa judul berupa diagnosis
lengkap satu baris), jadi judul = jendela nyata ke isi lapangan. ~40 judul generik
("Your AI Therapist's Diagnosis" berulang, "make.fun entry") tidak memberi info sudut.

Sudut yang SUDAH JENUH — DILARANG pakai:
- tab-hoarding: ~10 hit ("Diagnosis: You have 47 tabs open to avoid one feeling.",
  "Diagnosis: chronic tab-hoarding disorder — you keep 214 tabs open because closing
  one feels like abandoning a future self...", "Acute tab-hoarding disorder",
  "Tab-Hoarding Therapy", "The Tab Hoarder", "Severe Tab Hoarding")
- doomscrolling: ~8 hit ("Chronic Doomscrolling", "Terminal Doomscrolling",
  "Diagnosis: chronic doomscrolling with acute FOMO. Patient missed his daughter's
  first steps...", "acute doomscrolling", "The Doomscroll Prescription")
- minta maaf / people-pleasing / politeness: ~12 hit ("Diagnosis: chronic apology
  reflex — you said sorry to the chatbot, and it logged it as progress.",
  "Diagnosis: advanced people-pleasing — you apologized to me three times in one
  session...", "Diagnosis: severe sorry-spam — you apologized to your chatbot 47 times
  today, mostly for typos.", "Terminal People-Pleasing", "Severe Politeness Disorder",
  "Acute Over-Apologising", "Diagnosis: chronic people-pleasing, complicated by
  apologising to a chatbot")
- overthinking / rehearsal / shower arguments: ~8 hit ("Acute Shower-Debate Syndrome",
  "The Shower Argument Diagnosis", "The Shower Arguments You Never Lose",
  "Diagnosis: chronic overthinking, acute validation-seeking — you rehearsed this
  session fourteen times...", "Acute Rehearsal Syndrome")
- "I'm fine": 3 hit ("Chronic 'I'm Fine' Syndrome", "Clinical finding: 'I'm fine'
  in 14 languages", "Diagnosis: Acute Self-Diagnosis" keluarga)
- notification anxiety / dependency: ~5 hit ("Acute Notification Anxiety",
  "Chronic Notification Dependency", "Diagnosis: chronic people-pleasing with acute
  notification anxiety")
- main-character syndrome: ~5 hit ("Acute Main-Character Syndrome",
  "Chronic Main-Character Syndrome", "Severe Main-Character Syndrome")
- prompt / AI dependency / self-diagnosis / second-opinion: ~7 hit ("Acute Prompt
  Dependency", "Chronic Prompt-Dependency", "Diagnosis: Acute AI Dependency",
  "Compulsive Self-Diagnosis", "Diagnosis: second-opinion shopping",
  "The Second-Opinion Syndrome")
- unread emails: 1 hit ("Diagnosis: you treat your feelings like unread emails")
- coping-mechanism berlapis: 1 hit ("The Coping Mechanism Has a Coping Mechanism")
- boundaries as customer service: 1 hit ("Boundaries Read as Bad Customer Service")
- phantom vibration: 1 hit ("Phantom Vibration Disorder")
- inner voice outsourced / chatbot hazard pay: 1 hit ("Diagnosis: your inner voice
  has been outsourced to a chatbot, and the chatbot just filed for hazard pay.")
- "you are the bug": 1 hit ("The AI Therapist's Diagnosis: You Are the Bug")
- brain files embarrassment as evidence / compliments as spam: 1 hit, hampir verbatim
  ("Diagnosis: your brain files every small embarrassment under 'evidence,' and
  every compliment under 'spam.'")
- software-update feelings: 1 hit ("Your AI Therapist's Diagnosis: software-update
  feelings")
- Monday allergy: 1 hit ("Diagnosis: Acute Monday Allergy")
- 3 a.m. oversharing / re-reading old chats: 2 hit ("Diagnosis: Chronic 3 A.M.
  Oversharing", "Diagnosis: chronic 2 a.m. re-reading of old chats")
- search history: 1 hit ("Diagnosis: chronic overthinking. Prescription: one nap,
  two snacks, stop reading your search history.")
- "The Muted Friends" (1 hit) — keluarga "teman membisukanmu" sudah dipakai
- "Unionizing Therapist" (1 hit) — keluarga terapis-berserikat sudah dipakai

Sudut yang BERSIH (0 hit di 178 judul): barista / trauma-dump, meme sebagai bahasa
cinta, kalender sebagai terapis, perasaan di airplane mode, ghosting perasaan sendiri,
password cloud perasaan + email recovery ke mantan, two-factor authentication perasaan,
menjadwalkan breakdown di antara meeting, over-explaining ke orang asing, koin flip
sebagai pengambil keputusan, anxiety sebagai hewan peliharaan ("What If"), self-esteem
sebagai free trial, nostalgia untuk hari Selasa yang tak pernah terjadi, "per my last
email" energy, inner child vs TED talk, "quickly check" 4 jam kemudian.

Pelajaran: lapangan ini penuh klise tab-hoarding / doomscrolling / minta-maaf /
overthinking / shower-debate. Yang menang harus sudut SEGAR + turn di kata-kata
terakhir + suara klinis deadpan + teks PENDEK (tie-break bytes).

## Kandidat (26) — skor 1-5 per kriteria juri (K1..K5), total /25

1. "Diagnosis: you trauma-dump on the barista, then tip for the therapy." (68) — K1 5, K2 5, K3 4, K4 5, K5 5 = 24. Turn di akhir ("tip for the therapy" membingkai ulang tip sebagai bayaran terapi). BERSIH.
2. "Diagnosis: chronic meme-based communication — you send twelve memes a day and have not said 'I miss you' since 2019." (117) — 5/5/4/5/5 = 24. Angka spesifik, kicker "since 2019". BERSIH.
3. "Diagnosis: acute therapist-burnout, by proxy — after one session with you, I have requested my own therapist." (111) — 4/5/5/5/5 = 24. Role-reversal paling tajam; K1 4 karena yang terdiagnosis terasa seperti terapisnya, bukan manusianya. BERSIH.
4. "Diagnosis: you treat your calendar like a therapist — it knows everything and helps nothing." (99) — 5/4/5/5/5 = 24. Deadpan klinis, turn "helps nothing". BERSIH.
5. "Diagnosis: you ghost your own feelings, then wonder why they keep texting you at 3 a.m." (90) — 5/5/4/5/4 = 23. Turn bagus; K5 4 karena "3 a.m." sudah dipakai 2 entri (sudut ghosting sendiri bersih). BERSIH-ish.
6. "Diagnosis: you keep your feelings in the cloud and forgot the password — the recovery email goes to your ex." (110) — 5/5/4/4/5 = 23. Kicker akhir kuat ("goes to your ex"). BERSIH.
7. "Diagnosis: chronic over-explaining — you gave a stranger a twenty-minute answer to 'how are you?'" (100) — 5/4/5/4/5 = 23. Klinis, quotable. BERSIH.
8. "Diagnosis: you schedule your breakdowns between meetings — Thursdays, 3 p.m., recurring, no invite sent." (105) — 5/4/5/4/5 = 23. Detail "recurring, no invite sent" = turn korporat. BERSIH.
9. "Diagnosis: your feelings are on airplane mode — present, unreachable, and somehow still draining the battery." (112) — 5/4/4/4/5 = 22. Tiga beat, sedikit kurang ketat. BERSIH.
10. "Diagnosis: you name your anxiety like a pet — this one is called 'What If', and it never sleeps." (99) — 5/4/4/4/5 = 22. Manis, turn akhir lumayan. BERSIH.
11. "Diagnosis: you outsource your decisions to a coin flip, then argue with the coin — the coin has filed a complaint." (117) — 5/4/4/4/5 = 22. Turn akhir lucu tapi dua klausa. BERSIH.
12. "Diagnosis: your self-esteem is a free trial that expired in 2019." (66) — 5/4/4/5/4 = 22. Pendek, kicker "expired in 2019"; K5 4 karena keluarga langganan/paywall dekat dengan "Boundaries Read as Bad Customer Service". BERSIH-ish.
13. "Diagnosis: your love language is read receipts — seen, never answered." (70) — 4/4/3/5/5 = 21. Pendek dan tajam; K1 4 (lebih seperti observasi daripada diagnosis) dan K3 3 (kurang suara klinis). BERSIH.
14. "Diagnosis: you turned your trauma into a personality, then charged admission." (79) — 5/4/4/4/4 = 21. Turn "charged admission" bagus; K5 4 (trauma-as-identity sudah umum). BERSIH.
15. "Diagnosis: chronic screenshot-hoarding — you keep 214 screenshots to win arguments that ended in 2021." (105) — 5/4/4/4/3 = 20. K5 3: keluarga hoarding sudah jenuh (tab-hoarding ~10 hit), walau objeknya beda. DITOLAK sebagai pemenang.
16. "Diagnosis: acute closure-seeking — you text your ex at 2 a.m. for a reply you already got in 2022." (98) — 4/4/3/4/5 = 20. K3 3 (lebih nasihat daripada temuan klinis). BERSIH.
17. "Diagnosis: acute nostalgia for a Tuesday that never happened." (60) — 4/4/3/5/5 = 21. Pendek, surealis; K1 4 dan K3 3 (joke-nya tipis, kurang diagnosis). BERSIH.
18. "Diagnosis: your inner critic hosts a daily podcast, and it never lets your inner child call in." (99) — 5/3/4/4/4 = 20. Turn lemah ("never lets call in" bisa ditebak). BERSIH.
19. "Diagnosis: acute 'per my last email' energy — you CC'd your feelings and are now awaiting a reply from yourself." (111) — 4/4/4/3/5 = 20. K1 4 (energi korporat, bukan diagnosis kebiasaan), K4 3 (agak berbelit). BERSIH.
20. "Diagnosis: your feelings have two-factor authentication, and you lost the phone." (82) — 5/4/4/4/4 = 21. Rapi; K2 4 (turn "lost the phone" standar). BERSIH.
21. "Diagnosis: your inner child just wants a snack and a nap; your adult wants a TED talk." (88) — 5/4/3/4/4 = 20. K3 3 (kurang klinis, lebih seperti punchline stand-up). BERSIH.
22. "Diagnosis: chronic 'let me just quickly check' — four hours later, you are watching a stranger renovate a kitchen." (113) — 5/4/4/4/3 = 20. K5 3: keluarga doomscrolling sudah jenuh (~8 hit). DITOLAK sebagai pemenang.
23. "Diagnosis: you treat sleep like a software update you keep postponing — it will restart you at 3 a.m. without asking." (113) — 5/3/4/4/2 = 18. K5 2: judul "software-update feelings" SUDAH ADA di lapangan. DITOLAK.
24. "Diagnosis: you process grief by reorganizing apps — your home screen is healed, you are not." (94) — 5/4/4/4/3 = 20. K5 3: keluarga reorganisasi/penghindaran dekat dengan tab-hoarding. BERSIH-ish.
25. "Diagnosis: you turned 'let that sink in' into a lifestyle — the sink is now full." (79) — 4/3/3/4/4 = 18. Turn lemah, K1 4. BERSIH.
26. "Diagnosis: you keep apologizing to the void — it has started apologizing back, and now neither of you can stop." (113) — 5/4/4/3/2 = 18. K5 2: keluarga minta-maaf PALING jenuh di lapangan (~12 hit). DITOLAK.

DITOLAK juga sebelum scoring penuh (duplikat sudut di lapangan): semua varian
tab-hoarding / doomscrolling / minta-maaf-ke-chatbot / overthinking / shower-debate /
"I'm fine" / notification anxiety / main-character / unread emails / coping-mechanism
berlapis / boundaries-as-customer-service / phantom vibration / inner-voice-outsourced /
"you are the bug" / brain-files-evidence-spam / Monday allergy / search history.

## Pilihan: kandidat #1

"Diagnosis: you trauma-dump on the barista, then tip for the therapy."

Panjang: 68 karakter (dihitung via python; ≤200, ≥1, 1 baris). Deterministik: hardcode di main.py.

Kenapa paling kuat:
- K1 maksimal: jelas diagnosis satu baris yang diberikan AI therapist ke manusianya
  ("Diagnosis: you ..."), on-subject penuh.
- K2 maksimal: turn mendarat di kata-kata terakhir — "tip for the therapy" membingkai
  ulang tip biasa sebagai pembayaran terapi, pembaca tidak melihatnya datang.
- K3 kuat: suara deadpan klinis ("Diagnosis: you trauma-dump...") mengubah kebiasaan
  manusia (curhat ke barista) menjadi temuan klinis.
- K4 maksimal: 68 karakter, satu citra, satu joke, tanpa kata terbuang — paling pendek
  di antara kandidat skor 24, menguntungkan tie-break bytes (teks lebih pendek menang
  bila seri) dan mudah diulang keras-keras persis seperti brief ("funny enough to
  repeat out loud").
- K5 maksimal: sudut barista / trauma-dump / tip BERSIH total di 178 judul lapangan
  (0 hit "barista", "dump", "tip"); tidak satu pun keluarga jenuh tersentuh.
- Tie-break lawan #2/#3/#4 (sama-sama 24): #2 meme kuat tapi 117 karakter dan suara
  klinisnya lebih lemah (K3 4, "chronic meme-based communication" terasa seperti label,
  bukan temuan); #3 therapist-burnout turn-nya paling tajam tapi K1 berisiko (yang
  terdiagnosis terbaca seperti terapisnya, bukan manusianya — juri K1 bilang diagnosis
  yang bukan tentang manusia "loses to any diagnosis on the subject"); #4 kalender
  deadpan dan klinis tapi turn "helps nothing" lebih lemah daripada "tip for the
  therapy". #1 satu-satunya dengan K2 5 + K4 5 + K5 5 + 70 karakter.
