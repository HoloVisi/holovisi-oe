**Caveat**
This is an experimental project, only for the purpose of practice and testing, its code is heavily stolen from OpenELEC

[HoloVisi](http://www.holovisi.com)

# HoloVisi - Digital home, Open source, for Everyone


HoloVisi （中文名：和乐维视）= 嵌入式Linux + XBMC + 核心组件
* 嵌入式Linux：对包括内核（Kernel）在内的超过400个软件包进行交叉编译、测试，针对不同硬件平台进行优化，专门运行XBMC，以“从下至上”方式构建
* XBMC：是一个优秀的自由和开源的（GPL）媒体中心软件，创建于2003年，其目标是要成为HTPC（家庭影院）的最佳伴侣，该软件由遍布世界各地的自愿者开发维护。HoloVisi的策略是追踪其发行版本，以“补丁”方式进行改造
* 核心组件：将自开发的系统管理功能嵌入到XBMC中，并且内置若干媒体资源组件

**Source code**

* https://github.com/HoloVisi/holovisi-oe

**Installation**

* 

**Known issues**

* Testing snapshot

**License**

* HoloVisi is released under [GPLv2](http://www.gnu.org/licenses/gpl-2.0.html). Please refer to the "licenses" folder and 
  source code for clarification on upstream licensing.

**Copyright**

* Since HoloVisi includes code from many up stream projects it includes many 
  copyright owners. HoloVisi makes NO claim of copyright on any upstream code. 
  However all HoloVisi authored code is copyright holovisi.com.
  For a complete copyright list checkout the source code to examine the headers.
  Unless expressly stated otherwise all code submitted DIRECTLY to the HoloVisi 
  project (in any form) is licensed under [GPLv2](http://www.gnu.org/licenses/gpl-2.0.html) and the Copyright is donated to 
  holovisi.com.
  This allows the project to stay manageable in the long term by giving us the
  freedom to maintain the code as part of the whole without the management 
  overhead of preserving contact with every submitter ever e.g. move to GPLv3.
  You are absolutely free to retain copyright. To retain copyright simply add a 
  copyright header to every submitted code page.
  If you are submitting code that is not your own work it is the submitters 
  responsibility to place a header stating the copyright. 

**Features**

* 用户界面100%按家庭影院理念设计
* 开源且免费
* 超快启动，并针对多种平台进行优化
* 支持所有主流媒体格式
* 即插即用外部存储
* 家庭媒体中心：自动扫描、播放、管理局域网中的媒体文件
* 很容易安装到硬盘、SD卡、闪存（Flash）、USB等媒介
* 通过XBMC界面进行系统设置
* 通过组件扩展功能。组件类似Android应用，但开发难度远低于后者
* 中文本地化

**Software**

* XBMC HTPC software – View/Manage all your media.
* Samba server – File transfer from any PC client
* SSH server – Remote console access for debugging
* IR/Bluetooth Remote Control

**Notes**

* SSH login details are user: “root” password: “holovisi”.
  SSH allows command line access to your holovisi.com machine for configuration
  and file transfer. Linux/Mac clients can natively use SSH, while Windows
  users might want to try PuTTY for their terminal access.
  Starting with HoloVisi 2.0, SSH is disabled by default but all that is needed
  is an empty “ssh_enable” file to exist in /storage/.config to enable it.
* $HOME is mounted on /storage (the second ext4 partition on the drive). 
  All data transfered to the machine will go here, the rest of the system is
  read-only with the exception of /var (containing runtime configuration data).
* Manual update/downgrade procedure is as follows:
  Extract the snapshot and navigate to the 'target' directory.
  Copy KERNEL and SYSTEM along with KERNEL.md5 and SYSTEM.md5 to the 'Update' network share (or /storage/.update) on
  your holovisi machine. Your system will automatically upgrade during the 
  next reboot.
* Automatic mounting of filesystems is supported. Devices such as USB Flash 
  sticks can be plugged into a running machine and will be mounted to /media,
  showing up in xbmc’s GUI.
* Comments and questions are more than welcome, help is even better and patches 
  are absolutely perfect!!

**Questions/Support**

* Forums on [http://holovisi.com](http://holovisi.com)

**Happy HoloVisi'ing**
