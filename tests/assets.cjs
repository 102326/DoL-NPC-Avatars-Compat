const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict');
const root = path.resolve(__dirname,'..'), src = path.join(root,'src');
const text = fs.readFileSync(path.join(src,'game/base-system/NPCAvatarIcon.twee'),'utf8');
const paths = new Set();
for (const [,p] of text.matchAll(/(?<!@)src="([^"]+)"/g)) paths.add(p);
for (const [,expr] of text.matchAll(/@src="([^"]+)"/g)) {
  // These expressions are inspected string concatenations, not arbitrary mod scripts.
  for (const pronoun of ['m','f']) for (const hair of ['_lo','_po'])
  for (const color of ['bl','st']) for (const glasses of ['_co','_br','_gl'])
  for (const state of ['active','haunt','despair']) for (const loot of ['clothes','food','lurker','trash','valuables']) {
    const npc = new Proxy({}, {get(){return {pronoun}}});
    paths.add(Function('C','V','_sydiconhair','_sydiconhairC','_sydiconglasses','_bird_loot_select',`return (${expr})`)({npc},{wraith:{state}},hair,color,glasses,loot));
  }
}
const missing = [...paths].filter(p=>!fs.existsSync(path.join(src,p)));
const dormantMissing = ['img/misc/icon/social/sydney/syd_iwb_st.png'];
const unexpectedMissing = missing.filter(p=>!dormantMissing.includes(p));
const report = {checkedPaths:paths.size,missing,unexpectedMissing,dormantBranch:'Sydney mimic is marked unimplemented in the original mod; current vanilla game only assigns Robin, Kylar and Eden as mimics. Missing strawberry-blond non-haunt Sydney mimic asset retained as an explicit limitation.',scope:'Literal and finite dynamic portrait paths: m/f, Sydney hair/glasses, Wraith states, five standard Hawk loot values. Does not prove reachability of every expression or all game states.'};
fs.writeFileSync(path.join(__dirname,'asset-evidence.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify(report));
assert.deepEqual(unexpectedMissing,[]);
