# TODO
# - /etc/env.d/PATH does not support "merging",
#   so therefore we use /etc/profile.d
# - better name for subpackage?
%include	/usr/lib/rpm/macros.perl
Summary:	Perl wrapper which colorizes the output of the gcc/g++ compiler
Summary(pl):	Program koloruj±cy komunikaty kompilatorów gcc/g++
Name:		colorgcc
Version:	1.3.2
Release:	7.5
License:	GPL
Group:		Development/Tools
Source0:	http://home.i1.net/~jamoyers/software/colorgcc/%{name}-%{version}.tar.gz
# Source0-md5:	7d62f92ab99c8271c79c40a0a470e8f7
Patch0:		%{name}-paths.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_libdir	%{_prefix}/%{_lib}/%{name}

%description
colorgcc is a Perl wrapper that colorizes the output of the gcc/g++
compiler.

Read %{_defaultdocdir}/%{name}-%{version}/INSTALL after installing colorgcc.

%description -l pl
colorgcc to napisany w Perlu program opakowuj±cy (wrapper), który
koloruje tekst wypisywany przez kompilatory gcc/g++ podczas
kompilacji.

Po zainstalowaniu tego pakietu warto przeczytaæ
%{_defaultdocdir}/%{name}-%{version}/INSTALL .

%package wrapper
Summary:	Symlinks for c++/cc/g++/gcc
Summary(pl):	Dowi±zania symboliczne do c++/cc/g++/gcc
Group:		Development/Tools

%description wrapper
This package contains the softlinks to colorgcc for each compiler you
want to colorize.

%description wrapper -l pl
Ten pakiet zawiera dowi±zania symboliczne do colorgcc dla ka¿dego z
koloruj±cych kompilatorów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/etc/profile.d}

install colorgcc $RPM_BUILD_ROOT%{_bindir}

for cc in cc c++ g++ gcc %{__cc} %{__cxx}; do
	ln -s ../../bin/colorgcc $RPM_BUILD_ROOT%{_libdir}/$cc
done

echo 'export PATH=%{_libdir}:$PATH' > \
	$RPM_BUILD_ROOT/etc/profile.d/%{name}.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL ChangeLog CREDITS colorgccrc
%attr(755,root,root) %{_bindir}/colorgcc

%files wrapper
%defattr(644,root,root,755)
/etc/profile.d/%{name}.sh
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/*
