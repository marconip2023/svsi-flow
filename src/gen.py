import html
K='aJIs39okLTRsQMwk96NWrC'
def fig(i): return f'https://www.figma.com/design/{K}/SVSI?node-id={i.replace(":","-")}'
def proto(i): return f'https://www.figma.com/proto/{K}/SVSI?page-id=0%3A1&node-id={i.replace(":","-")}&starting-point-node-id={i.replace(":","%3A")}&scaling=scale-down-width&content-scaling=fixed'
FLOWS={ # key: (node, role, label) — mirrors the Figma prototype starting points
 'Q1':('6:2','buyer','Supplier List → filters → details'),
 'Q2':('2100:5389','buyer','Supplier Detail tabs'),
 'Q3':('2069:4926','buyer','Remove From SVSI'),
 'Q4':('832:18557','buyer','Factory Detail → Moving out of SVSI'),
 'Q5':('1060:24230','buyer','Factory Detail → Add to SVSI Task'),
 'Q6':('2224:17113','buyer','Check application → approve / return / reject'),
 'Q7':('1405:9212','buyer','Review result → confirm, generate, preview → send'),
 'Q8':('5415:45423','buyer','Preview → send to SVSI team'),
 'Q10':('5022:33099','buyer','Returned by SVSI → fix → resend'),
 'Q11':('1654:21336','buyer','Final review → upload signed → complete now or later'),
 'S1':('3009:38379','supplier','Apply for SVSI, start to submit'),
 'S2':('3662:12154','supplier','Item list bulk actions'),
 'S3':('3012:39313','supplier','View submitted application'),
 'S4':('1043:21409','supplier','Application returned → edit'),
 'S5':('1043:21574','supplier','Application rejected'),
 'S6':('1656:22338','supplier','Upload signed Agreement & Addendum'),
 'S7':('40:22271','supplier','Factory List → filters → Factory detail'),
 'L1':('291:3947','lab','Assessment List, filter & sort'),
 'L2':('3012:40666','lab','Confirm assessment date → upload result → complete'),
 'L3':('3047:43791','lab','Upload revised report'),
 'T1':('1603:18989','team','SVSI team review → return / reject / confirm'),
 'E1':('3028:11319','team','Ethical review: grade & upload'),
 'E2':('5179:41959','team','Returned by SVSI → re-review → confirm'),
}
ROLE={'buyer':'QT','supplier':'Supplier','lab':'Lab','team':'SVSI / Ethical'}
PREF={'Q':'QT','S':'Supplier','L':'Lab','E':'Ethical','T':'SVSI'}
def flowname(k): return f'{PREF[k[0]]} {k[1:]} · {FLOWS[k][2]}'
def play(k):
  n,r,l=FLOWS[k]
  return f'<a class="play {r}" href="{proto(n)}" target="_blank" rel="noopener"><span class="tri" aria-hidden="true"></span><span class="pk">{PREF[k[0]]} {k[1:]}</span>{html.escape(l)}</a>'
def card(shot,i,title,body,alt):
  return f'''    <div class="frame">
      <a class="shot" href="{fig(i)}" target="_blank" rel="noopener"><img src="shots/{shot}" alt="{html.escape(alt)}" loading="lazy"></a>
      <div class="body">
        <h3>{title}</h3>
        <p>{body}</p>
        <a class="go" href="{fig(i)}" target="_blank" rel="noopener">Open in Figma <span class="id">{i}</span></a>
      </div>
    </div>'''
def more(head,items):
  li='\n'.join(f'      <li><a href="{fig(i)}" target="_blank" rel="noopener"><span class="nm">{n}</span><span class="id">{i}</span></a></li>' for n,i in items)
  return f'''  <div class="morelinks">
    <div class="mh">{head}</div>
    <ul>
{li}
    </ul>
  </div>'''
def chip(r,t): return f'<span class="chip {r}"><span class="dot"></span>{t}</span>'
def step(sid,num,h2,actors,intro,plays,cards,mores):
  return f'''<section class="step" id="{sid}">
  <div class="stephead">
    <span class="stepnum">{num}</span>
    <div>
      <h2>{h2}</h2>
      <div class="actors">{''.join(chip(r,t) for r,t in actors)}</div>
    </div>
  </div>
  <p class="intro">{intro}</p>
  <div class="plays"><span class="pl">Play the prototype</span>{''.join(play(k) for k in plays)}</div>
  <div class="frames">
{chr(10).join(card(*c) for c in cards)}
  </div>
{chr(10).join(more(*m) for m in mores)}
</section>'''

S=[]
S.append(step('s0','00','Before the task exists',[('buyer','QT')],
 'SVSI applies to a <strong>factory</strong>, not a supplier. So the buyer starts from the supplier list, expands a supplier to see the factories underneath it, and decides which of those factories are in scope. Adding a factory to SVSI puts it at <strong>Not Rated</strong>; the scheme is set after the assessment. Factories that will never join are marked <strong>Non-Participating</strong>.',
 ['Q1','Q3','Q4','Q5','Q2'],
 [('s01_supplier_list.png','530:3455','Supplier list, expanded','Each supplier row opens to the factories under it. Every factory carries its own SVSI scheme chip, and the SVSI Scheme column filter narrows the list by tier (there are no tier tabs).','Supplier list expanded to show the factories under each supplier'),
  ('s02_mark_svsi.png','952:3937','Add to or remove from SVSI','Bulk-select factories, then use Actions. Adding confirms first and lands every factory at <code>NOT RATED</code>; removing moves it to <code>NON-PARTICIPATING</code>.','Selecting out-of-scope factories before adding them to SVSI'),
  ('s27_waiting_supplier.png','8025:31778','Added, waiting for the supplier','Right after QT adds a factory, the task sits at <code>Need to Start SVSI</code>. Until the supplier submits the application there is no task to show: the Tasks tab reads <strong>Tasks (0)</strong> and a single card says the supplier has not applied yet.','Factory page while the supplier has not applied')],
 [('Also in this area',[('Supplier list, collapsed (default view)','6:2'),('Add To SVSI, confirm','3744:15578'),('Add To SVSI, done','2075:12383'),('Remove From SVSI, confirm','2078:5392'),('Factory detail, overview','832:18557'),('Supplier detail, overview','2100:5389')])]))
S.append(step('s1','01','Application',[('supplier','Supplier applies'),('buyer','QT checks')],
 'The supplier starts the application themselves. This is the part that used to be the Word <em>Application Form v4</em>. They confirm the factory, run a self-assessment, pick the items the factory wants to self-inspect, and give payer details. The buyer then reviews the whole submission and either approves it, returns it for correction, or rejects it.',
 ['S1','S2','S3','S4','S5','Q6'],
 [('s03_app_part1.png','140:166','Part 1, factory &amp; contact','First-year applicants give the full factory record. Renewals carry most of it forward.','Application part 1, first year'),
  ('s04_self_assess.png','144:165','Self-assessment','The factory declares it meets the entry criteria. A "not met" answer blocks the application there rather than later.','Self-assessment with all criteria met'),
  ('s05_item_list.png','2534:7740','Item list','Products are added from a dialog. Per row: first shipped date and the previous inspection party (self-inspection or a third-party lab). SVSI product category and 1506 return % are filled later by QT. Several rows can be filled at once with bulk actions; on a narrow screen the table scrolls sideways.','Item list with products added'),
  ('s06_payer.png','147:162','Payer information','Replaces the <em>Payer Information Form</em> doc. ICW bills the supplier on TBGASL\'s behalf, so this has to be right before the invoice is raised.','Payer information form'),
  ('s07_buyer_check.png','149:162','QT check form','QT reads the whole submission on one page and decides: approve and continue, return, or reject.','QT check form review screen')],
 [('States and variants',[('Item list, nothing added yet','2532:7007'),('Add product dialog','2536:7173'),('Bulk action menu','3331:12973'),('Bulk fill, ship date','3331:13503'),('Bulk fill, inspection party','3331:14033'),('Self-assessment, criteria not met','144:336'),('Preview before submit','2556:24543'),('Application submitted','2556:23682'),('Returned to the supplier for correction','1043:21409'),('Rejected by the SVSI team','1043:21574')])]))
S.append(step('s2','02','Invoice',[('buyer','QT raises'),('supplier','Supplier pays')],
 'The fee depends on the tier being applied for. The invoice reads <strong>Bronze &middot; USD 950 / factory</strong>, so <code>Scheme / Fee</code> is known from this step onward, well before any tier is awarded. Payment must clear before the assessment starts; fees are non-refundable even if the application is later refused.',
 ['Q6'],
 [('s08_invoice.png','1189:30008','Invoice, pending payment','Task basic information on top, invoice details and the priced inspection plan below. One factory, one line.','QT invoice screen, pending payment')],
 [('Also in this step',[('Supplier side, invoice paid','403:3910'),('Booking reserved, assessment date set','1339:5441'),('Returned to previous stage','1177:28333'),('Application rejected','1177:27905')])]))
S.append(step('s3','03','Lab Assessment',[('lab','Lab &middot; UL Assessment')],
 'The lab has its own view with its own lifecycle: <em>Pending Assessment &rarr; In Progress &rarr; In Progress - Upload Report &amp; Result &rarr; Assessment Completed</em>. They confirm the assessment date, run the on-site factory assessment, then upload the report with <strong>two results</strong>, each with its own result, date and remark. <strong>Findings are optional</strong>: Major NC, Minor NC and Observation / OFI entries are added only if there are any. The report result decides the next step: <strong>Pass &rarr; the ethical team is notified</strong> and the task goes to Ethical Check; <strong>Fail &rarr; straight to QT Review</strong>, with no ethical check.',
 ['L1','L2','L3'],
 [('s09_lab_detail.png','3012:40666','Lab task detail','The lab\'s working screen for one factory assessment task. Actions opens Update Status.','Lab task detail for a factory assessment'),
  ('s10_lab_upload.png','1390:4580','Upload result &amp; report','Empty state first. Each result takes a result, date and remark. Update &amp; Upload stays disabled until a result is chosen.','Lab upload result and report, empty state')],
 [('The rest of the lab flow',[('Lab home dashboard','291:3947'),('Assessment list','291:2582'),('Assessment list, Task Status filter','3697:14554'),('Assessment list, sort by date','3706:15161'),('Select update type','291:8393'),('Confirm assessment date','376:3134'),('Uploaded, result and findings','376:3970'),('Complete, confirm','376:4611'),('Upload revised report','1455:11943')])]))
S.append(step('s4','04','Ethical Check',[('team','Ethical team')],
 'Ethical Check now runs <strong>before</strong> QT Review and is no longer optional: when the lab report is <strong>Pass</strong> the ethical team is notified (fixed contacts, so QT no longer types an e-mail) and the task waits at <code>Result Review (Ethical)</code>. The ethical team picks an <strong>ethical grade</strong> (Satisfactory, Needs Improvement, Satisfactory after Critical or Critical), the grade date, a remark and documents, reconfirms, and the task moves on to QT. The grade does not change the flow for now. When the report is <strong>Fail</strong> this step is skipped and Ethical Check stays grey on the progress bar.',
 ['E1','E2'],
 [('s28_ethical_empty.png','3028:11319','Ethical review, empty','Basic information on top; grade, grade date, remark and documents below. Confirm stays disabled until a grade and date are given.','Ethical review form, empty'),
  ('s29_ethical_grade.png','9445:32448','Grade dropdown','Four grades to choose from. A grade, not a score.','Ethical grade dropdown open'),
  ('s30_ethical_filled.png','2028:8302','Ethical review, filled','Grade, date, remark and documents in; Confirm opens the reconfirm dialog.','Ethical review form, filled')],
 [('Ethical team screens',[('Grade date picker','4950:21039'),('Reconfirm before submitting','3785:22004'),('Returned by SVSI team, re-review','5179:41959'),('Retired: QT chose ethical or SVSI','9504:32819')])]))
S.append(step('s5','05','QT Review, Documents &amp; Preview',[('buyer','QT')],
 'QT reads the lab\'s report and result and, when there is one, the <strong>ethical result</strong>, shown read-only as <em>3. Ethical Review</em> in Confirm Result and in the Review tab. If the report needs work, QT requests a revised report or rejects the task. Otherwise QT does everything in one pass: <strong>confirms the result</strong> with a remark and the item list, fills the <strong>Agreement and Addendum in one step</strong>, then <strong>previews</strong> all of it and sends it to the SVSI team. The two documents are generated as <strong>two separate PDFs</strong>. A <strong>Fail</strong> report comes here directly: there is no Ethical Review section and Ethical Check stays grey, but QT can still confirm and continue, return the report or reject the task.',
 ['Q7','Q8'],
 [('s11_qt_review.png','4990:22447','Confirm result','Remark, documents, the read-only Ethical Review and the items for final approval in one dialog. QT fills 1506 return %, first shipped date, previous inspection party and the SVSI product category for seasonal items, and sees <strong>Fail Inspection</strong> (Yes / No) per item. The table scrolls sideways instead of squeezing columns.','Confirm result dialog'),
  ('s31_qt_fail.png','9524:33668','Report Fail, straight to QT','<code>Result Review (QT)</code> without an ethical check: Ethical Check is grey and the Review tab reads No data now.','Task page when the lab report is Fail'),
  ('s24_gen_agreement.png','4990:23021','Generate Agreement &amp; Addendum','One form for both documents: parties, factory, dates and sign information. TBGASL signatories are fixed. There is no supplier signatory field: the supplier fills in their name and title when they sign offline.','Generate Agreement and Addendum step'),
  ('s19_qt_preview.png','5415:45423','Preview, then send','Result and remark, the Addendum product list, the Agreement &amp; Addendum details, and the two generated PDFs to preview or download. Send to the SVSI team.','QT preview of result, agreement and addendum'),
  ('s25_qt_import.png','5453:23476','Export &amp; import item data','For long item lists, QT exports the table to Excel, fills SVSI product category, 1506 return %, first shipped to TBG, inspection party and QT comment offline, then imports it back. The file can\'t have more items than the list; if it does, an error alert blocks the import.','Import item data dialog, file ready')],
 [('Steps and other decisions',[('Review lab result','1405:9212'),('Returned by SVSI, scroll table','5022:33099'),('Wide screen (1920), full table','7361:31251'),('Dev note, item tables scroll','7356:29010'),('Request revised report','1448:9588'),('Reject task','1448:9626')]),
  ('Report Fail (no ethical result)',[('Confirm result, report Fail','9524:32557'),('Report return','9524:37875'),('QT reject','9524:37874'),('Generate, preview &amp; complete without ethical','9535:32810')]),
  ('Export &amp; import',[('Item list exported (toast)','5453:22001'),('Import, choose file','5453:22717'),('Import, file ready','5453:23476'),('Import, too many items','5453:24225'),('Item list imported','5453:24976')])]))
S.append(step('s6','06','SVSI Team Review',[('team','SVSI Team')],
 'The SVSI team approves <strong>once</strong>. They see everything QT prepared, including the ethical grade when there is one, and can return the task to QT or to the ethical team (also when there is no ethical result yet), or reject it. When they confirm, a preview shows QT\'s remark, documents, item list, Agreement and Addendum. If something is off, they leave a <strong>comment on the item</strong> (visible to QT only) instead of sending it back; for long lists the comments can be exported to Excel and imported back. Before confirming they <strong>tick which documents go to the supplier</strong>: a renewal usually needs the Addendum only, because the Agreement stays valid. With nothing ticked, Confirm is disabled.',
 ['T1','Q10'],
 [('s13_svsi_review.png','1603:18989','Result review','Reject task, return to QT, return to ethical team, or open the preview to confirm.','SVSI team review screen'),
  ('s21_svsi_preview.png','4976:23490','Preview &amp; comment','Same preview as QT, read-only, with an SVSI comment per item, a checkbox per document to choose what is sent to the supplier, and a place for the SVSI team\'s own remark and documents.','SVSI preview with item comments'),
  ('s26_svsi_import.png','5461:25722','Export &amp; import comments','Same Export / Import pop-up as QT, but only SVSI Comment is imported; changes to any other column are ignored by the backend. Same rule on row count.','SVSI import dialog, too many items')],
 [('Decisions',[('Return to QT','5425:22371'),('Return to ethical team','5415:45329'),('Reject task','1649:20424'),('Nothing ticked, Confirm disabled','7383:30351'),('No ethical result','9524:37882'),('Returned to QT, ethical graded','5163:38457'),('Returned to QT, no ethical grade','9524:34016')]),
  ('Export &amp; import',[('Item list exported (toast)','5461:23686'),('Import, choose file','5461:24347'),('Import, file ready','5461:25033'),('Import, too many items','5461:25722'),('Comments imported','5461:26416'),('Dev note','5457:23692')])]))
S.append(step('s7','07','Supplier Signs',[('supplier','Supplier')],
 'The supplier downloads the documents the SVSI team sent (Agreement and / or Addendum, as two PDFs), signs them offline and uploads the signed copies back into ICW. Choosing a new file replaces the previous one. The task waits at <strong>Pending Sign Off</strong> until the signed copies arrive.',
 ['S6'],
 [('s17_supplier_sign.png','1656:22338','Pending sign off','Sent automatically when the SVSI team confirms. Upload opens the signed-copy dialog.','Supplier task page with documents to sign')],
 [('The signing route',[('Upload signed Agreement &amp; Addendum','3692:16071'),('Signed copies submitted','3692:16294'),('No ethical result (report Fail)','9535:35378')])]))
S.append(step('s8','08','QT Final Review &amp; Complete',[('buyer','QT'),('supplier','Supplier sees result')],
 'The signed copies come back to QT at <strong>Final Review (QT)</strong>. QT uploads the countersigned copy; a dialog then offers <strong>Complete task</strong> right away, or <strong>Confirm later</strong> from the task page. That closes the task, awards the tier and makes the <strong>self-inspection validity date live</strong>. Before the validity start date the factory still uses third-party inspection.',
 ['Q11'],
 [('s22_qt_final.png','1654:21336','Final review (QT)','Signed copies on file and waiting for QT.','QT final review'),
  ('s23_complete_after_upload.png','5415:46438','Complete now or later','Right after QT uploads the signed copy: complete the task now, or choose Confirm later and finish from the task page.','Complete task dialog after upload'),
  ('s15_complete_task.png','1654:21831','Complete task','Complete Task asks for confirmation, because the tier and the validity window cannot be changed afterwards.','Task page ready to complete'),
  ('s16_completed.png','1656:22657','Completed','The factory\'s scheme is awarded and the validity dates appear on the factory record.','Completed task')],
 [('After completion',[('Complete Task dialog','1794:3978'),('Supplier sees it completed','2771:29996'),('Factory list after completion','3576:14235'),('No ethical result (report Fail)','9535:32810')])]))

idx=[]
for role,keys in [('buyer',[k for k in FLOWS if k[0]=='Q']),('supplier',[k for k in FLOWS if k[0]=='S']),('lab',[k for k in FLOWS if k[0]=='L']),('team',[k for k in FLOWS if k[0] in 'TE'])]:
  idx.append(f'<div class="pgroup"><div class="pgh">{chip(role,ROLE[role])}<span class="cnt">{len(keys)} flows</span></div><div class="plist">'+''.join(play(k) for k in keys)+'</div></div>')
E2E=f'<a class="e2e" href="{proto("952:3937")}" target="_blank" rel="noopener"><span class="tri" aria-hidden="true"></span><span class="et"><b>End-to-end, everything approved</b><span>Set SVSI factory &rarr; Application &rarr; Invoice &rarr; Lab Assessment &rarr; Ethical Check (report Pass) &rarr; QT confirms, generates the documents &amp; previews &rarr; SVSI Team reviews once &rarr; Supplier signs &rarr; QT final review &amp; completes. Switch role with the Lab / Buyer / Supplier chips in the top bar, or press &rarr;.</span></span></a>'
PROTO='\n'.join(idx)

# ---------- status by role ----------
ST=[
 ('Factory invited to SVSI', ('Need to Start SVSI', 'n'), ('Need to Start SVSI', 'n'), None),
 ('Supplier submits; can still edit', ('Application Submitted', 'w'), ('Application Submitted', 'i'), None),
 ('QT opens the check form', ('Under Review', 'w'), ('Under Review', 'i'), None),
 ('QT returns it for correction', ('Application Returned', 'i'), ('Application Returned', 'w'), None),
 ('QT approves; invoice being issued', ('Pending Invoice', 'i'), ('Pending Invoice', 'i'), None),
 ('Invoice issued, waiting for payment', ('Pending Payment', 'i'), ('Pending Payment', 'w'), None),
 ('Paid; lab to book the assessment', ('Pending Assessment', 'i'), ('In Progress', 'i'), ('Pending Assessment', 'n')),
 ('Assessment date confirmed; assessment and report', ('Pending Assessment', 'i'), ('In Progress', 'i'), ('In Progress', 'i')),
 ('Lab uploads the report and result', ('Pending Assessment', 'i'), ('In Progress', 'i'), ('In Progress - Upload Report & Result', 'i')),
 ('Report PASS: ethical team is notified and gives the ethical grade', ('Result Review (Ethical)', 'w'), ('In Progress', 'i'), ('Assessment Completed', 'i')),
 ('Report FAIL: goes straight to QT (no ethical check, Ethical Check stays grey)', ('Result Review (QT)', 'w'), ('In Progress', 'i'), ('Assessment Completed', 'i')),
 ('QT reviews (sees the ethical result), confirms, generates the documents and previews', ('Result Review (QT)', 'w'), ('In Progress', 'i'), ('Assessment Completed', 'i')),
 ('QT asks for a revised report', ('Report Return', 'i'), ('In Progress', 'i'), ('Revise Report', 'w')),
 ('SVSI team reviews once and comments on items', ('Result Review (SVSI)', 'w'), ('In Progress', 'i'), ('Assessment Completed', 'i')),
 ('Waiting for the supplier to sign', ('Pending Sign Off', 'w'), ('Pending Sign Off', 'w'), ('Assessment Completed', 'i')),
 ('Signed copies back; QT final review', ('Final Review (QT)', 'w'), ('Final Review (QT)', 'w'), ('Assessment Completed', 'i')),
 ('Task completed; validity goes live', ('Completed', 's'), ('Completed', 's'), ('Assessment Completed', 'i')),
 ('Application or task rejected', ('Rejected', 'e'), ('Rejected', 'e'), None),
]
def stc(x):
  if not x: return '<td class="none">&mdash;</td>'
  tbc=' <span class="tbc">TBC</span>' if len(x)>2 else ''
  return f'<td><span class="st {x[1]}"><i></i>{html.escape(x[0])}</span>{tbc}</td>'
rows='\n'.join(f'<tr><th scope="row"><span class="sn">{i+1:02d}</span>{html.escape(a)}</th>{stc(b)}{stc(c)}{stc(d)}</tr>' for i,(a,b,c,d) in enumerate(ST))
STATUS=f"""<div class="tablewrap stwrap"><table class="sttable">
<thead><tr><th>Stage</th><th><span class="chip buyer"><span class="dot"></span>QT &middot; SVSI Team</span></th><th><span class="chip supplier"><span class="dot"></span>Supplier</span></th><th><span class="chip lab"><span class="dot"></span>Lab</span></th></tr></thead>
<tbody>
{rows}
</tbody></table></div>"""

tpl=open('tpl.html').read()
out=tpl.replace('%%STEPS%%','\n\n'.join(S)).replace('%%PROTO%%',PROTO).replace('%%E2E%%',E2E).replace('%%STATUS%%',STATUS).replace('%%FIGMA%%',fig('0:1'))
open('index.html','w').write(out)
print(len(out))
