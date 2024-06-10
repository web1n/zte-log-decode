# 中兴机顶盒日志解码工具

这个脚本用来解码中兴机顶盒（ZTE B860AV3.2-U）通过 系统设置-保存系统日志到 U 盘 功能获取到的日志文件。

## 使用方法

1. 将您的日志文件保存在与脚本相同的目录中，或者提供日志文件的路径。

2. 在命令行中运行脚本：

   ```sh
   python decode.py <input_file>
   ```

   将 `<input_file>` 替换为您的日志文件的名称或路径。

3. 解码后的内容将保存在一个新文件中，该文件的名称为原文件名后加上 `.decoded`。

### 示例

如果您有一个名为 `ULog_1.log` 的日志文件，可以通过运行以下命令进行解码：

```sh
python decode.py ULog_1.log
```

解码后的内容将保存在 `ULog_1.log.decoded` 文件中。

解码前：
```
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: prjr.lva.TkllvtaVhtveazkl: wrznvu ak tkllvta ak nktrnykba/127.0.0.1 (ekca 9667) rwavc 5000mb: zbTkllvtavu wrznvu: VTKLLCVWQBVU (Tkllvtazkl cvwqbvu)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra nzstkcv.zk.ZkSczuxv.zbTkllvtavu(ZkSczuxv.prjr:223)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra nzstkcv.zk.ZkSczuxv.tkllvtaVcclk(ZkSczuxv.prjr:161)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra nzstkcv.zk.ZkSczuxv.tkllvta(ZkSczuxv.prjr:112)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra prjr.lva.EnrzlBktovaZmen.tkllvta(EnrzlBktovaZmen.prjr:192)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra prjr.lva.EnrzlBktovaZmen.tkllvta(EnrzlBktovaZmen.prjr:459)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra prjr.lva.Bktova.tkllvta(Bktova.prjr:843)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.Enrawkcm.tkllvtaBktova(Enrawkcm.prjr:152)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.Tkllvtazkl.tkllvta(Tkllvtazkl.prjr:101)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeVlxzlv.tkllvta(YaaeVlxzlv.prjr:294)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeVlxzlv.bvluBktovaCvdqvba(YaaeVlxzlv.prjr:255)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeVlxzlv.bvluCvdqvba(YaaeVlxzlv.prjr:206)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeQCNTkllvtazklZmen.vhvtqav(YaaeQCNTkllvtazklZmen.prjr:345)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeQCNTkllvtazklZmen.tkllvta(YaaeQCNTkllvtazklZmen.prjr:89)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.rluckzu.koyaae.zlavclrn.yaae.YaaeQCNTkllvtazklZmen.xvaKqaeqaBacvrm(YaaeQCNTkllvtazklZmen.prjr:197)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.tvcaqb.kaabas.dkbmklnkruvc.r.v.r(BkqctvWznv:117)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra tkm.tvcaqb.kaabas.dkbmklnkruvc.dkbmkl.r.cql(BkqctvWznv:149)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: 	ra prjr.nrlx.Aycvru.cql(Aycvru.prjr:841)
06-10 13:14:11.639  5784  9658 I Bgbavm.vcc: Trqbvu sg: nzstkcv.zk.VcclkVhtveazkl: zbTkllvtavu wrznvu: VTKLLCVWQBVU (Tkllvtazkl cvwqbvu)
06-10 13:14:11.649  5784  9658 I Bgbavm.vcc: 	ra nzstkcv.zk.ZkSczuxv.zbTkllvtavu(ZkSczuxv.prjr:208)
06-10 13:14:11.649  5784  9658 I Bgbavm.vcc: 	... 16 mkcv
```

解码后：
```
06-10 13:14:11.639  5784  9658 W System.err: java.net.ConnectException: failed to connect to localhost/127.0.0.1 (port 9667) after 5000ms: isConnected failed: ECONNREFUSED (Connection refused)
06-10 13:14:11.639  5784  9658 W System.err: 	at libcore.io.IoBridge.isConnected(IoBridge.java:223)
06-10 13:14:11.639  5784  9658 W System.err: 	at libcore.io.IoBridge.connectErrno(IoBridge.java:161)
06-10 13:14:11.639  5784  9658 W System.err: 	at libcore.io.IoBridge.connect(IoBridge.java:112)
06-10 13:14:11.639  5784  9658 W System.err: 	at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:192)
06-10 13:14:11.639  5784  9658 W System.err: 	at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:459)
06-10 13:14:11.639  5784  9658 W System.err: 	at java.net.Socket.connect(Socket.java:843)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.Platform.connectSocket(Platform.java:152)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.Connection.connect(Connection.java:101)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpEngine.connect(HttpEngine.java:294)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpEngine.sendSocketRequest(HttpEngine.java:255)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpEngine.sendRequest(HttpEngine.java:206)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:345)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:89)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.android.okhttp.internal.http.HttpURLConnectionImpl.getOutputStream(HttpURLConnectionImpl.java:197)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.certus.ottstb.qosmonloader.a.e.a(SourceFile:117)
06-10 13:14:11.639  5784  9658 W System.err: 	at com.certus.ottstb.qosmonloader.qosmon.a.run(SourceFile:149)
06-10 13:14:11.639  5784  9658 W System.err: 	at java.lang.Thread.run(Thread.java:841)
06-10 13:14:11.639  5784  9658 W System.err: Caused by: libcore.io.ErrnoException: isConnected failed: ECONNREFUSED (Connection refused)
06-10 13:14:11.649  5784  9658 W System.err: 	at libcore.io.IoBridge.isConnected(IoBridge.java:208)
06-10 13:14:11.649  5784  9658 W System.err: 	... 16 more
```
