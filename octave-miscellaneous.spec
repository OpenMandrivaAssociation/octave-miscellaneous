%define	pkgname miscellaneous
%define name	octave-%{pkgname}
%define version 1.0.11

Summary:	Miscellaneous Octave tools that don't fit elsewhere
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/miscellaneous/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.16
BuildRequires:  octave-devel >= 2.9.16
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:	termcap-devel

%description
Miscellaneous Octave tools that don't fit elsewhere.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}


%changelog
* Wed Jun 29 2011 Lev Givon <lev@mandriva.org> 1.0.11-1mdv2011.0
+ Revision: 688079
- Update to 1.0.11.

* Wed Jun 29 2011 Lev Givon <lev@mandriva.org> 1.0.10-1
+ Revision: 688048
- import octave-miscellaneous


