%global octpkg miscellaneous

Summary:	Miscellaneous tools that don't fit somewhere else
Name:		octave-%{octpkg}
Version:	1.3.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.6.0
BuildRequires:	ncurses-devel
#BuildRequires:	termcap-devel
BuildRequires:	units

Requires:	octave(api) = %{octave_api}
Requires:	units

Requires(post): octave
Requires(postun): octave

%description
Miscellaneous tools that don't fit somewhere else.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

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

