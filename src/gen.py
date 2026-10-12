import html
K='aJIs39okLTRsQMwk96NWrC'
def fig(i): return f'https://www.figma.com/design/{K}/SVSI?node-id={i.replace(":","-")}'
def proto(i): return f'https://www.figma.com/proto/{K}/SVSI?page-id=0%3A1&node-id={i.replace(":","-")}&starting-point-node-id={i.replace(":","%3A")}&scaling=scale-down-width&content-scaling=fixed'
FLOWS={ # key: (node, role, label)
 'B1':('6:2','buyer','Supplier List → filters → details'),
 'B2':('2100:5389','buyer','Supplier Detail tabs'),
 'B3':('2069:4926','buyer','Remove From SVSI'),
 'B4':('832:18557','buyer','Factory Detail → Moving out of SVSI'),
 'B5':('1060:24230','buyer','Factory Detail → Add to SVSI Task'),
 'B6':('2224:17113','buyer','Check application → approve / return / reject'),
 'B7':('1405:9212','buyer','QT review lab result → confirm / revise / reject'),
 'B8':('1603:19804','buyer','Generate Agreement → upload → complete task'),
 'S1':('3009:38379','supplier','Apply for SVSI, start to submit'),
 'S2':('3662:12154','supplier','Item list bulk actions'),
 'S3':('3012:39313','supplier','View submitted application'),
 'S4':('1043:21409','supplier','Application returned → edit'),
 'S5':('1043:21574','supplier','Application rejected'),
 'S6':('1656:22338','supplier','Upload signed Agreement & Addendum'),
 'S7':('40:22271','supplier','Factory List → filters → Factory detail'),
 'L1':('291:3947','lab','Audit List, filter & sort'),
 'L2':('3012:40666','lab','Confirm audit date → upload result → complete'),
 'L3':('3047:43791','lab','Upload revised report'),
 'E1':('3028:11319','team','Ethical review & upload'),
 'T1':('1603:18989','team','SVSI Team review → confirm / return / reject'),
}
ROLE={'buyer':'Buyer','supplier':'Supplier','lab':'Lab','team':'SVSI / Ethical'}
PREF={'B':'Buyer','S':'Supplier','L':'Lab','E':'Ethical','T':'SVSI Team'}
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
S.append(step('s0','00','Before the task exists',[('buyer','Buyer')],
 'SVSI applies to a <strong>factory</strong>, not a supplier. So the buyer starts from the supplier list, expands a supplier to see the factories underneath it, and decides which of those factories are in scope. Adding a factory to SVSI puts it at <strong>Not Rated</strong>; the scheme is set after the audit. Factories that will never join are marked <strong>Out of Scope</strong>.',
 ['B1','B3','B4','B5','B2'],
 [('s01_supplier_list.png','530:3455','Supplier list, expanded','Each supplier row opens to the factories under it. Every factory carries its own SVSI scheme chip, and the scheme tabs filter the list by tier.','Supplier list expanded to show the factories under each supplier'),
  ('s02_mark_svsi.png','952:3937','Add to or remove from SVSI','Bulk-select factories, then use Actions. Adding confirms first and lands every factory at <code>NOT RATED</code>; removing moves it to <code>OUT OF SCOPE</code>.','Selecting out-of-scope factories before adding them to SVSI')],
 [('Also in this area',[('Supplier list, collapsed (default view)','6:2'),('Add To SVSI, confirm','3744:15578'),('Add To SVSI, done','2075:12383'),('Remove From SVSI, confirm','2078:5392'),('Factory detail, overview','832:18557'),('Supplier detail, overview','2100:5389')])]))
S.append(step('s1','01','Application',[('supplier','Supplier applies'),('buyer','Buyer checks')],
 'The supplier starts the application themselves. This is the part that used to be the Word <em>Application Form v4</em>. They confirm the factory, run a self-assessment, pick the items the factory wants to self-inspect, and give payer details. The buyer then reviews the whole submission and either approves it, returns it for correction, or rejects it.',
 ['S1','S2','S3','S4','S5','B6'],
 [('s03_app_part1.png','140:166','Part 1, factory &amp; contact','First-year applicants give the full factory record. Renewals carry most of it forward.','Application part 1, first year'),
  ('s04_self_assess.png','144:165','Self-assessment','The factory declares it meets the entry criteria. A "not met" answer blocks the application there rather than later.','Self-assessment with all criteria met'),
  ('s05_item_list.png','2534:7740','Item list','Products are added from a dialog. Per row: first shipped date and who inspects, self-inspection or a third-party lab. Several rows can be filled at once with bulk actions.','Item list with products added'),
  ('s06_payer.png','147:162','Payer information','Replaces the <em>Payer Information Form</em> doc. ICW bills the supplier on TBGASL\'s behalf, so this has to be right before the invoice is raised.','Payer information form'),
  ('s07_buyer_check.png','149:162','Buyer check form','The buyer reads the whole submission on one page and decides: approve and continue, return, or reject.','Buyer check form review screen')],
 [('States and variants',[('Item list, nothing added yet','2532:7007'),('Add product dialog','2536:7173'),('Bulk action menu','3331:12973'),('Bulk fill, ship date','3331:13503'),('Bulk fill, inspection party','3331:14033'),('Self-assessment, criteria not met','144:336'),('Preview before submit','2556:24543'),('Application submitted','2556:23682'),('Returned to the supplier for correction','1043:21409'),('Rejected by the SVSI team','1043:21574')])]))
S.append(step('s2','02','Invoice',[('buyer','Buyer raises'),('supplier','Supplier pays')],
 'The fee depends on the tier being applied for. The invoice reads <strong>Bronze &middot; USD 950 / factory</strong>, so <code>Scheme / Fee</code> is known from this step onward, well before any tier is awarded. Payment must clear before the assessment starts; fees are non-refundable even if the application is later refused.',
 ['B6'],
 [('s08_invoice.png','1189:30008','Invoice, pending payment','Task basic information on top, invoice details and the priced inspection plan below. One factory, one line.','Buyer invoice screen, pending payment')],
 [('Also in this step',[('Supplier side, invoice paid','403:3910'),('Booking reserved, audit date set','1339:5441'),('Returned to previous stage','1177:28333'),('Application rejected','1177:27905')])]))
S.append(step('s3','03','Lab Audit',[('lab','Lab &middot; UL / BV')],
 'The lab has its own view with its own lifecycle: <em>Received &rarr; Audit Scheduled &rarr; Audit Completed &rarr; Report Uploaded</em>. They confirm the audit date, run the on-site factory assessment, then upload the report and the result. <strong>Findings are optional</strong>: Major NC, Minor NC and Observation / OFI entries are added only if there are any.',
 ['L1','L2','L3'],
 [('s09_lab_detail.png','3012:40666','Lab task detail','The lab\'s working screen for one factory audit task. Actions opens Update Status.','Lab task detail for a factory audit'),
  ('s10_lab_upload.png','1390:4580','Upload result &amp; report','Empty state first. Update &amp; Upload stays disabled until a result is chosen. Audit data is entered once, not re-keyed per report.','Lab upload result and report, empty state')],
 [('The rest of the lab flow',[('Lab home dashboard','291:3947'),('Audit list','291:2582'),('Audit list, Task Status filter','3697:14554'),('Audit list, sort by date','3706:15161'),('Select update type','291:8393'),('Confirm audit date','376:3134'),('Uploaded, result and findings','376:3970'),('Complete, confirm','376:4611'),('Upload revised report','1455:11943')])]))
S.append(step('s4','04','QT Review',[('buyer','Buyer &middot; WBA QT')],
 'QT reads the lab\'s report and result and takes one of three routes: <strong>confirm</strong> and move on, <strong>request a revised report</strong> from the lab, or <strong>reject</strong> it. Only once the result is confirmed does the task carry an Audit Result, an Audit Report Completed Date, and a findings summary.',
 ['B7'],
 [('s11_qt_review.png','1405:9212','Report &amp; result','Result, findings breakdown and the lab\'s documents on one page, under the task\'s own Basic information.','Buyer reviewing the uploaded report and result')],
 [('The three decisions',[('Confirm result','1043:23844'),('Request revised report','1448:9588'),('Reject task','1448:9626')])]))
S.append(step('s5','05','Ethical Check',[('buyer','Buyer sends'),('team','Ethical team reviews')],
 'A separate annual product performance review, run alongside the factory audit rather than inside it. Phase 1 is an uploaded SVSI evaluation spreadsheet judged on 1506 for 52 weeks, VOC, star rating and the past year\'s inspection history. Phase 2 is meant to replace that upload with figures pulled from ICW for the buyer to verify.',
 ['E1','B7'],
 [('s12_ethical.png','3374:62256','Send to ethical team','The buyer sends the task to the ethical team. The review type, criteria and items in scope sit on the page, so the reviewer knows what they are judging.','Task page with the Ethical Check action')],
 [('After the check',[('Ethical review, empty','3028:11319'),('Ethical review, filled','2028:8302'),('Ethical check complete','1455:11275')])]))
S.append(step('s6','06','SVSI Team Review',[('team','SVSI Team')],
 'The final gate before documents are issued. TBGASL has sole discretion over whether a supplier joins the programme; accepting payment is not acceptance into SVSI. The team can confirm, return the task to QA or to the ethical team, or reject it.',
 ['T1'],
 [('s13_svsi_review.png','1603:18989','Team review','Everything the earlier steps produced, in one place. Final Confirm opens the Confirm Result dialog, where products can still be added or removed.','SVSI team review screen')],
 [('Decisions',[('Confirm result','1603:19480'),('Return to QA','1649:20385'),('Return to ethical team','1603:19556'),('Reject application','1649:20424')])]))
S.append(step('s7','07','Approve &amp; Sign',[('buyer','Buyer generates'),('supplier','Supplier signs'),('team','SVSI Team completes')],
 'Two documents come out of ICW. The <strong>Agreement</strong> is supplier-level and first-year only. The <strong>Addendum</strong> is factory-level and renewed every year; it lists exactly which products that factory may self-inspect. The supplier signs offline, the scans come back into ICW, and <strong>Complete task</strong> stamps the self-inspection validity dates and awards the tier.',
 ['B8','S6'],
 [('s14_gen_addendum.png','1773:4050','Generate Addendum','Step 2 of the generate dialog. Every field from the Word template in one form; products are picked here.','Generate addendum dialog with products'),
  ('s15_complete_task.png','1654:21831','Complete task','The signed documents are in. Complete Task asks for confirmation, because the tier and the validity window cannot be changed afterwards.','Task page ready to complete'),
  ('s16_completed.png','1656:22657','Completed','The factory\'s current scheme is set and the validity dates appear on the factory record.','Completed task with the scheme awarded')],
 [('The signing route',[('Generate Agreement, step 1','1769:4050'),('Signed documents, ready to upload','1654:21336'),('Upload signed Agreement &amp; Addendum','3629:12009'),('Upload again','3702:15199'),('Supplier signs and uploads','1656:22338'),('Supplier sees the task completed','2771:29996'),('Factory list after completion','3576:14235')])]))

idx=[]
for role,keys in [('buyer',[k for k in FLOWS if k[0]=='B']),('supplier',[k for k in FLOWS if k[0]=='S']),('lab',[k for k in FLOWS if k[0]=='L']),('team',[k for k in FLOWS if k[0] in 'ET'])]:
  idx.append(f'<div class="pgroup"><div class="pgh">{chip(role,ROLE[role])}<span class="cnt">{len(keys)} flows</span></div><div class="plist">'+''.join(play(k) for k in keys)+'</div></div>')
E2E=f'<a class="e2e" href="{proto("952:3937")}" target="_blank" rel="noopener"><span class="tri" aria-hidden="true"></span><span class="et"><b>End-to-end, everything approved</b><span>Set SVSI factory &rarr; Application &rarr; Invoice &rarr; Lab Audit &rarr; QT Review &rarr; Ethical Check &rarr; SVSI Team Review &rarr; Supplier signs &rarr; Complete. Switch role with the Lab / Buyer / Supplier chips in the top bar, or press &rarr;.</span></span></a>'
PROTO='\n'.join(idx)
tpl=open('tpl.html').read()
out=tpl.replace('%%STEPS%%','\n\n'.join(S)).replace('%%PROTO%%',PROTO).replace('%%E2E%%',E2E).replace('%%FIGMA%%',fig('0:1'))
open('index.html','w').write(out)
print(len(out))
