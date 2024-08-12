export memory memory(initial: 2, max: 0);

global g_a:int = 66592;
export global heap_base:int = 66592;
export global data_end:int = 1052;

table T_a:funcref(min: 8, max: 8);

data d_a(offset: 1024) =
  "\01\00\00\00\02\00\00\00\03\00\00\00\04\00\00\00\05\00\00\00\06\00\00\00"
  "\07\00\00\00";

import function env_putc_js(a:int);

function f_b() {
}

function f_c(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 2;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 0;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 2;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:byte_ptr = g[3]:int;
  ha[0] = ga;
  var ia:int_ptr = g[2]:int;
  ia[0] = ea;
  g[6]:int = da;
  label B_a:
  var ja:int = g[6]:int;
  return ja;
}

function f_d(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 2;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 1;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 2;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:int = -1;
  var ka:int = ia ^ ja;
  var la:byte_ptr = g[3]:int;
  la[0] = ka;
  var ma:int_ptr = g[2]:int;
  ma[0] = ea;
  g[6]:int = da;
  label B_a:
  var na:int = g[6]:int;
  return na;
}

function f_e(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 3;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 2;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 3;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:ubyte_ptr = g[5]:int;
  var ka:int = ja[2];
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = ia ^ ma;
  var oa:byte_ptr = g[3]:int;
  oa[0] = na;
  var pa:int_ptr = g[2]:int;
  pa[0] = ea;
  g[6]:int = da;
  label B_a:
  var qa:int = g[6]:int;
  return qa;
}

function f_f(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 3;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 3;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 3;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:ubyte_ptr = g[5]:int;
  var ka:int = ja[2];
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = ia & ma;
  var oa:byte_ptr = g[3]:int;
  oa[0] = na;
  var pa:int_ptr = g[2]:int;
  pa[0] = ea;
  g[6]:int = da;
  label B_a:
  var qa:int = g[6]:int;
  return qa;
}

function f_g(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 3;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 4;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 3;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:ubyte_ptr = g[5]:int;
  var ka:int = ja[2];
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = ia | ma;
  var oa:byte_ptr = g[3]:int;
  oa[0] = na;
  var pa:int_ptr = g[2]:int;
  pa[0] = ea;
  g[6]:int = da;
  label B_a:
  var qa:int = g[6]:int;
  return qa;
}

function f_h(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 3;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 5;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 3;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[1];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:ubyte_ptr = g[5]:int;
  var ka:int = ja[2];
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = ia + ma;
  var oa:byte_ptr = g[3]:int;
  oa[0] = na;
  var pa:int_ptr = g[2]:int;
  pa[0] = ea;
  g[6]:int = da;
  label B_a:
  var qa:int = g[6]:int;
  return qa;
}

function f_i(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  var h:int = 3;
  g[5]:int = a;
  g[4]:int = b;
  g[3]:int = c;
  g[2]:int = d;
  var i:int = g[4]:int;
  var j:int = h;
  var k:int = i;
  var l:int = j > k;
  var m:int = l;
  if (eqz(m)) goto B_b;
  var n:int = 105;
  g[6]:int = n;
  goto B_a;
  label B_b:
  var o:int = 6;
  var p:ubyte_ptr = g[5]:int;
  var q:int = p[0];
  g[31]:byte = q;
  var r:int = g[31]:ubyte;
  var s:int = 255;
  var t:int = r & s;
  var u:int = 15;
  var v:int = t & u;
  var w:int = 255;
  var x:int = v & w;
  var y:int = o;
  var z:int = x;
  var aa:int = y != z;
  var ba:int = aa;
  if (eqz(ba)) goto B_c;
  var ca:int = 112;
  g[6]:int = ca;
  goto B_a;
  label B_c:
  var da:int = 0;
  var ea:int = 3;
  var fa:ubyte_ptr = g[5]:int;
  var ga:int = fa[2];
  var ha:int = 255;
  var ia:int = ga & ha;
  var ja:ubyte_ptr = g[5]:int;
  var ka:int = ja[1];
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = ia - ma;
  var oa:int = 255;
  var pa:int = na & oa;
  var qa:byte_ptr = g[3]:int;
  qa[0] = pa;
  var ra:int_ptr = g[2]:int;
  ra[0] = ea;
  g[6]:int = da;
  label B_a:
  var sa:int = g[6]:int;
  return sa;
}

function f_j(a:int, b:int, c:int, d:int, e:int):int {
  var f:int = g_a;
  var g:int = 64;
  var h:int = f - g;
  g_a = h;
  var i:int = 0;
  h[13]:int = a;
  h[12]:int = b;
  h[11]:int = c;
  h[10]:int = d;
  h[9]:int = e;
  h[8]:int = i;
  var j:int = h[13]:int;
  h[7]:int = j;
  h[6]:int = i;
  loop L_b {
    var k:int = 0;
    var l:int = h[7]:int;
    var m:int = h[13]:int;
    var n:int = h[12]:int;
    var o:int = m + n;
    var p:int = l;
    var q:int = o;
    var r:int = p < q;
    var s:int = r;
    var t:int = k;
    if (eqz(s)) goto B_c;
    var u:int = h[6]:int;
    var v:int = h[10]:int;
    var w:int = u;
    var x:int = v;
    var y:int = w < x;
    t = y;
    label B_c:
    var z:int = t;
    var aa:int = 1;
    var ba:int = z & aa;
    if (eqz(ba)) goto B_d;
    var ca:int = 7;
    var da:ubyte_ptr = h[7]:int;
    var ea:int = da[0];
    h[63]:byte = ea;
    var fa:int = h[63]:ubyte;
    var ga:int = 255;
    var ha:int = fa & ga;
    var ia:int = 15;
    var ja:int = ha & ia;
    h[23]:byte = ja;
    var ka:int = h[23]:ubyte;
    var la:int = 255;
    var ma:int = ka & la;
    var na:int = ca;
    var oa:int = ma;
    var pa:int = na <= oa;
    var qa:int = pa;
    if (eqz(qa)) goto B_e;
    var ra:int = 112;
    h[14]:int = ra;
    goto B_a;
    label B_e:
    var sa:int = 0;
    var ta:int = 15;
    var ua:int = h + ta;
    var va:int = ua;
    var wa:int = 8;
    var xa:int = h + wa;
    var ya:int = xa;
    var za:int = 0;
    var ab:int = 1024;
    var bb:int = h[23]:ubyte;
    var cb:int = 255;
    var db:int = bb & cb;
    var eb:int = 2;
    var fb:int = db << eb;
    var gb:int_ptr = ab + fb;
    var hb:int = gb[0];
    h[4]:int = hb;
    h[15]:byte = za;
    h[2]:int = sa;
    var ib:int = h[4]:int;
    var jb:int = h[7]:int;
    var kb:int = h[12]:int;
    var lb:int = h[7]:int;
    var mb:int = h[13]:int;
    var nb:int = lb - mb;
    var ob:int = kb - nb;
    var pb:int = call_indirect(jb, ob, va, ya, ib);
    var qb:int = sa;
    var rb:int = pb;
    var sb:int = qb != rb;
    var tb:int = sb;
    if (eqz(tb)) goto B_f;
    goto B_d;
    label B_f:
    var ub:int = h[15]:ubyte;
    var vb:int = 255;
    var wb:int = ub & vb;
    var xb:int = h[11]:int;
    var yb:int = h[6]:int;
    var zb:ubyte_ptr = xb + yb;
    var ac:int = zb[0];
    var bc:int = 24;
    var cc:int = ac << bc;
    var dc:int = cc >> bc;
    var ec:int = wb;
    var fc:int = dc;
    var gc:int = ec == fc;
    var hc:int = gc;
    if (eqz(hc)) goto B_g;
    var ic:int = h[8]:int;
    var jc:int = 1;
    var kc:int = ic + jc;
    h[8]:int = kc;
    label B_g:
    var lc:int = h[2]:int;
    var mc:int = h[7]:int;
    var nc:int = mc + lc;
    h[7]:int = nc;
    var oc:int = h[6]:int;
    var pc:int = 1;
    var qc:int = oc + pc;
    h[6]:int = qc;
    continue L_b;
    label B_d:
  }
  var rc:int = h[7]:int;
  var sc:int = h[13]:int;
  var tc:int = h[12]:int;
  var uc:int = sc + tc;
  var vc:int = rc;
  var wc:int = uc;
  var xc:int = vc != wc;
  var yc:int = xc;
  if (eqz(yc)) goto B_i;
  var zc:int = 0;
  var ad:byte_ptr = h[9]:int;
  ad[0] = zc;
  goto B_h;
  label B_i:
  var bd:int = h[8]:int;
  var cd:int = h[10]:int;
  var dd:int = bd;
  var ed:int = cd;
  var fd:int = dd != ed;
  var gd:int = fd;
  if (eqz(gd)) goto B_k;
  var hd:int = 0;
  var id:byte_ptr = h[9]:int;
  id[0] = hd;
  goto B_j;
  label B_k:
  var jd:int = 1;
  var kd:byte_ptr = h[9]:int;
  kd[0] = jd;
  label B_j:
  label B_h:
  var ld:int = 0;
  h[14]:int = ld;
  label B_a:
  var md:int = h[14]:int;
  var nd:int = 64;
  var od:int = h + nd;
  g_a = od;
  return md;
}

export function Match(a:int, b:int, c:int, d:int):int {
  var e:int = g_a;
  var f:int = 32;
  var g:int = e - f;
  g_a = g;
  var h:int = 0;
  var i:int = 11;
  var j:int = g + i;
  var k:int = j;
  var l:int = 0;
  g[6]:int = a;
  g[5]:int = b;
  g[4]:int = c;
  g[3]:int = d;
  g[11]:byte = l;
  var m:int = g[6]:int;
  var n:int = g[5]:int;
  var o:int = g[4]:int;
  var p:int = g[3]:int;
  var q:int = f_j(m, n, o, p, k);
  var r:int = h;
  var s:int = q;
  var t:int = r != s;
  var u:int = t;
  if (eqz(u)) goto B_b;
  var v:int = 0;
  g[7]:int = v;
  goto B_a;
  label B_b:
  var w:int = g[11]:ubyte;
  var x:int = 1;
  var y:int = w & x;
  g[7]:int = y;
  label B_a:
  var z:int = g[7]:int;
  var aa:int = 32;
  var ba:int = g + aa;
  g_a = ba;
  return z;
}

export function writev_c(a:int, b:int, c:int):int {
  var d:int = g_a;
  var e:int = 32;
  var f:int_ptr = d - e;
  g_a = f;
  var g:int = 0;
  f[7] = a;
  f[6] = b;
  f[5] = c;
  f[4] = g;
  f[3] = g;
  loop L_b {
    var h:int = f[3];
    var i:int = f[5];
    var j:int = h;
    var k:int = i;
    var l:int = j < k;
    var m:int = l;
    if (eqz(m)) goto B_a;
    var n:int = 0;
    f[2] = n;
    loop L_d {
      var o:int = f[2];
      var p:int = f[6];
      var q:int = f[3];
      var r:int = 3;
      var s:int = q << r;
      var t:int_ptr = p + s;
      var u:int = t[1];
      var v:int = o;
      var w:int = u;
      var x:int = v < w;
      var y:int = x;
      if (eqz(y)) goto B_c;
      var z:int = f[6];
      var aa:int = f[3];
      var ba:int = 3;
      var ca:int = aa << ba;
      var da:int_ptr = z + ca;
      var ea:int = da[0];
      var fa:int = f[2];
      var ga:ubyte_ptr = ea + fa;
      var ha:int = ga[0];
      var ia:int = 24;
      var ja:int = ha << ia;
      var ka:int = ja >> ia;
      env_putc_js(ka);
      var la:int = f[2];
      var ma:int = 1;
      var na:int = la + ma;
      f[2] = na;
      continue L_d;
    }
    label B_c:
    var oa:int = f[6];
    var pa:int = f[3];
    var qa:int = 3;
    var ra:int = pa << qa;
    var sa:int_ptr = oa + ra;
    var ta:int = sa[1];
    var ua:int = f[4];
    var va:int = ua + ta;
    f[4] = va;
    var wa:int = f[3];
    var xa:int = 1;
    var ya:int = wa + xa;
    f[3] = ya;
    continue L_b;
  }
  label B_a:
  var za:int = f[4];
  var ab:int = 32;
  var bb:int = f + ab;
  g_a = bb;
  return za;
}

