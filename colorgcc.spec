# TODO
# - /etc/env.d/PATH does not support "merging",
#   so therefore we use /etc/profile.d
# - better name for subpackage?
Summary:	Perl wrapper which colorizes the output of the gcc/g++ compiler
Summary(hu.UTF-8):	Perl wrapper, amely a gcc/g++ fordítók kimeneteit színezi
Summary(pl.UTF-8):	Program kolorujący komunikaty kompilatorów gcc/g++
Name:		colorgcc
Version:	1.3.2
Release:	9
License:	GPL
Group:		Development/Tools
Source0:	http://home.i1.net/~jamoyers/software/colorgcc/%{name}-%{version}.tar.gz
# Source0-md5:	7d62f92ab99c8271c79c40a0a470e8f7
URL:		http://www.schlueters.de/colorgcc.html
Patch0:		%{name}-paths.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/%{name}

%description
colorgcc is a Perl wrapper that colorizes the output of the gcc/g++
compiler.

%description  -l hu.UTF-8
colorgcc egy perl wrapper, amely a gcc/g++ fordítók kimeneteit
színezi.

%description -l pl.UTF-8
colorgcc to napisany w Perlu program opakowujący (wrapper), który
koloruje tekst wypisywany przez kompilatory gcc/g++ podczas
kompilacji.

%package wrapper
Summary:	Symlinks for c++/cc/g++/gcc
Summary(hu.UTF-8):	Szimbolikus linkek c++/cc/g++/gcc-hez
Summary(pl.UTF-8):	Dowiązania symboliczne do c++/cc/g++/gcc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description wrapper
This package contains the softlinks to colorgcc for each compiler you
want to colorize.

%description wrapper -l hu.UTF-8
Ez a csomag tartalmazza a szimbolikus linkeket a colorgcc-hez minden
fordítóhoz, amit színezni akarsz.

%description wrapper -l pl.UTF-8
Ten pakiet zawiera dowiązania symboliczne do colorgcc dla każdego z
kolorowanych kompilatorów.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},/etc/profile.d}

install colorgcc $RPM_BUILD_ROOT%{_bindir}

for cc in cc c++ g++ gcc %{_target_cpu}-pld-linux-gcc %{_target_cpu}-pld-linux-g++; do
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
%attr(755,root,root) /etc/profile.d/%{name}.sh
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/*
