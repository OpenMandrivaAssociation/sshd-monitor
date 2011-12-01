%define	name	sshd-monitor
%define	version	0.3

Summary:	A simple monitor for sshd
Name:		%{name}
Version:	%{version}
Release:	%mkrel 9
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
rm -rf %{buildroot}
install expect-sshd -D %{buildroot}%{_datadir}/%{name}/expect-sshd
install sshd-restarter -D %{buildroot}%{_datadir}/%{name}/sshd-restarter
install -m 644 cron.entry -D %{buildroot}%{_sysconfdir}/cron.d/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README.CVS
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}


