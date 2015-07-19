%define	name	sshd-monitor
%define	version	0.3

Summary:	A simple monitor for sshd
Name:		%{name}
Version:	%{version}
Release:	17
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Monitoring
Requires:	openssh-server
Requires:	telnet-client
Requires:	expect
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A very basic sshd monitor written in expect.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install expect-sshd -D $RPM_BUILD_ROOT%{_datadir}/%{name}/expect-sshd
install sshd-restarter -D $RPM_BUILD_ROOT%{_datadir}/%{name}/sshd-restarter
install -m 644 cron.entry -D $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README.CVS
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mdv2011.0
+ Revision: 670026
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2011.0
+ Revision: 607561
- rebuild

* Wed Apr 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-7mdv2010.1
+ Revision: 540214
- requires telnet-client virtual package

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2010.1
+ Revision: 524125
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3-5mdv2010.0
+ Revision: 427215
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 225475
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2008.1
+ Revision: 179531
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3-2mdv2007.0
+ Revision: 114743
- mkrel

* Sun Jan 02 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.3-1mdk
- be sure to send the identification string to avoid a log
from openssh (bug #12552).

