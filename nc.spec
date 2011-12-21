Summary: Reads and writes data across network connections using TCP or UDP
Name: nc
Version: 1.84
Release: 22%{?dist}
URL:	 http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/nc/
# source is CVS checkout
# CVSROOT=anoncvs@anoncvs1.usa.openbsd.org:/cvs cvs co -D 2005-10-26 src/usr.bin/nc
# there are also some files from older CVS checkouts in tarball.
Source0: nc-%{version}.tar.bz2
# an email with some patches has been sent to upstream
# - email can be found in openbsd tech list archive from January 2010
#   (registration needed)
# patch 0 is Fedora specific
Patch0: nc-1.84-glib.patch
# patch 1 sent in the mail
Patch1: nc-1.78-pollhup.patch
# patch 2 sent in the mail
Patch2: nc-1.82-reuseaddr.patch
# patch is Fedora specific
Patch3: nc-gcc_signess.patch
# patch 4 sent in the mail
Patch4: nc-1.84-connect_with_timeout.patch
# patch 5 sent in the mail
Patch5: nc-1.84-udp_stop.patch
# patch 6 sent in the mail
Patch6: nc-1.84-udp_port_scan.patch
# patch 7 sent in the mail
Patch7: nc-1.84-crlf.patch
# patch 8 sent in the mail
Patch8: nc-1.84-verb.patch
# patch 9 sent in the mail
Patch9: nc-1.84-man.patch
# patch is Fedora specific
Patch10: nc-1.84-gcc4.3.patch
# patch 11 sent in the mail
Patch11: nc-1.84-efficient_reads.patch
# patch 12 sent in the mail
Patch12: nc-1.84-verbose-segfault.patch

License: BSD
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glib2-devel
Requires: glib2

%description
The nc package contains Netcat (the program is actually nc), a simple
utility for reading and writing data across network connections, using
the TCP or UDP protocols. Netcat is intended to be a reliable back-end
tool which can be used directly or easily driven by other programs and
scripts.  Netcat is also a feature-rich network debugging and
exploration tool, since it can create many different connections and
has many built-in capabilities.

You may want to install the netcat package if you are administering a
network and you'd like to use its debugging and network exploration
capabilities.

%prep
%setup -q -n nc
%patch0 -p1 -b .glib
%patch1 -p1 -b .pollhup
%patch2 -p1 -b .reuseaddr
%patch3 -p1 -b .gcc
%patch4 -p1 -b .timeout
%patch5 -p1 -b .udp_stop
%patch6 -p0 -b .port_scan
%patch7 -p1 -b .crlf
%patch8 -p1 -b .verb
%patch9 -p1 -b .man
%patch10 -p1 -b .gcc
%patch11 -p1 -b .reads
%patch12 -p1 -b .verb-segfault

%build
gcc $RPM_OPT_FLAGS -Werror -fno-strict-aliasing `pkg-config --cflags --libs glib-2.0` netcat.c atomicio.c socks.c -o nc

%install
rm -rf ${RPM_BUILD_ROOT}
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 nc ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 644 nc.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/nc
%{_mandir}/man1/nc.1*
%doc README scripts

%changelog
* Tue Feb 09 2010 Jan Zeleny <jzeleny@redhat.com> - 1.84-22
- changed license and some new comments in spec file

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.84-21.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Jan Zeleny <jzeleny@redhat.com> - 1.84-21
- fixed segfault when listening to socket and -v enabled (#513925)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.84-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 03 2009 Jan Zeleny <jzeleny@redhat.com> - 1.84-19
- updated network reading to be more efficient (#493129)

* Fri Feb 27 2009 Jan Safranek <jsafrane@redhat.com> - 1.84-18
- fixed compilation with GCC 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.84-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.84-16
- Autorebuild for GCC 4.3

* Mon Jan  7 2008 Jan Safranek <jsafrane@redhat.com> - 1.84-15
- fixed compilation with gcc 4.3

* Wed Dec  5 2007 Radek Vokál <rvokal@redhat.com> - 1.84-14
- rebuilt

* Thu Aug 23 2007 Radek Vokál <rvokal@redhat.com> - 1.84-13
- rebuilt

* Wed Mar 14 2007 Radek Vokál <rvokal@redhat.com> - 1.84-12
- fix manpage for -C option (#203931)

* Tue Feb 13 2007 Radek Vokál <rvokal@redhat.com> - 1.84-11
- few spec file changes

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.84-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Radek Vokal <rvokal@redhat.com> - 1.84-9
- fix in crlf patch, -z option now works again (#207733)

* Tue Aug 29 2006 Radek Vokal <rvokal@redhat.com> - 1.84-8
- fix verbose option (#202321) <varmojfekoj@gmail.com>

* Mon Aug 28 2006 Radek Vokal <rvokal@redhat.com> - 1.84-7
- add dist tag
- add '-C' option and behaviour for sending CRLFs as line-ending (#203931) <koszorus@reidea.hu>

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.84-6.1
- rebuild

* Mon Jul 10 2006 Radek Vokal <rvokal@redhat.com> - 1.84-6
- improve UDP port scanning (#159119) <varmojfekoj@gmail.com>

* Mon Jul 10 2006 Radek Vokal <rvokal@redhat.com> - 1.84-5
- stop hanging when used as a UDP client (#188976) <varmojfekoj@gmail.com>

* Mon Mar 06 2006 Radek Vokál <rvokal@redhat.com> - 1.84-4
- timeout works also for connect (#182736)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.84-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.84-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 25 2006 Radek Vokal <rvokal@redhat.com> 1.84-3
- warnings cleaned-up, compile with -Werror

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Dec 07 2005 Radek Vokal <rvokal@redhat.com> 1.84-2
- fix build requires

* Fri Nov 18 2005 Radek Vokal <rvokal@redhat.com> 1.84-1
- follow upstream

* Fri Oct 21 2005 Radek Vokal <rvokal@redhat.com> 1.82-2
- use SO_REUSEADDR (#171315)

* Tue Sep 27 2005 Tomas Mraz <tmraz@redhat.com> 1.82-1
- update from OpenBSD upstream CVS
- fix pollhup patch so it reads everything before shutdown

* Wed May 11 2005 David Woodhouse <dwmw2@redhat.com> 1.78-2
- Don't ignore POLLHUP and go into an endless loop (#156835)

* Mon Apr 11 2005 Radek Vokal <rvokal@redhat.com> 1.78-1
- update from CVS, using glib functions

* Thu Mar 31 2005 Radek Vokal <rvokal@redhat.com> 1.77-1
- switching to new OpenBSD version of netcat

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> 1.10-25
- gcc4 rebuilt

* Wed Dec 22 2004 Radek Vokal <rvokal@redhat.com> 1.10-24
- enabling telnet support (#143498)
- removed static linking
- array range fixed

* Mon Nov 01 2004 Radek Vokal <rvokal@redhat.com> 1.10-23
- return value of help function fixed (#137785)

* Tue Sep 21 2004 Radek Vokal <rvokal@redhat.com> 1.10-22
- timeout option patch when SIGALRM blocked (#132973)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.10-17
- rebuild on all arches

* Tue Jul 23 2002 Bill Nottingham <notting@redhat.com> 1.10-16
- fix for the parsing patch (<eedmoba@eede.ericsson.se>)

* Thu Jul 18 2002 Bill Nottingham <notting@redhat.com> 1.10-15
- don't strip binaries
- fix parsing of some services (#52874) (<eedmoba@eede.ericsson.se>)
- fix man page (#63544)

