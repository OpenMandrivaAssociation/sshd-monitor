%define	name	sshd-monitor
%define	version	0.3
%define	release	%mkrel 2

Summary:	A simple monitor for sshd
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	openssh-server telnet expect
BuildArch:	noarch

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


