%global octpkg miscellaneous

Summary:	Miscellaneous tools that don't fit somewhere else
Name:		octave-miscellaneous
Version:	1.3.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/miscellaneous/
Source0:	https://downloads.sourceforge.net/octave/miscellaneous-%{version}.tar.gz

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	ncurses-devel
#BuildRequires:	termcap-devel
BuildRequires:	units


Requires:	octave(api) = %{octave_api}
Requires:	units

Requires(post): octave
Requires(postun): octave

%description
Miscellaneous tools that don't fit somewhere else.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

