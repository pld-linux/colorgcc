%include	/usr/lib/rpm/macros.perl
Summary:	perl wrapper which colorizes the output of the gcc/g++ compiler
Summary(pl):	program kolorujący komunikaty kompilatorów gcc/g++
Name:		colorgcc
Version:	1.3.2
Release:	2
Group:		Development/Tools
Group(pl):	Programowanie/Narzędzia
License:	GPL
Source:		http://home.i1.net/~jamoyers/software/colorgcc/%{name}-%{version}.tar.gz
Patch:		colorgcc-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-ANSIColor
BuildRoot:	/tmp/%{name}-%{version}-root

%description
colorgcc is a perl wrapper that colorizes the output of the gcc/g++ compiler.

Read %{_defaultdocdir}/INSTALL after installing colorgcc.

%description -l pl
colorgcc to napisany w perlu program opakowujący (wrapper), który
koloruje tekst wypisywany przez kompilatory gcc/g++ podczas kompilacji.

Po zainstalowaniu tego pakietu przeczytaj %{_defaultdocdir}/INSTALL.

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install colorgcc $RPM_BUILD_ROOT%{_bindir}

gzip -9nf INSTALL ChangeLog CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {INSTALL,ChangeLog,CREDITS}.gz colorgccrc

%attr(755,root,root) %{_bindir}/colorgcc
