%include	/usr/lib/rpm/macros.perl
Summary:	perl wrapper which colorizes the output of the gcc/g++ compiler
Summary(pl):	program koloruj±cy komunikaty kompilatorów gcc/g++
Name:		colorgcc
Version:	1.3.2
Release:	4
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
License:	GPL
Source0:	http://home.i1.net/~jamoyers/software/colorgcc/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl(Term::ANSIColor)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
colorgcc is a perl wrapper that colorizes the output of the gcc/g++
compiler.

Read %{_defaultdocdir}/INSTALL after installing colorgcc.

%description -l pl
colorgcc to napisany w perlu program opakowuj±cy (wrapper), który
koloruje tekst wypisywany przez kompilatory gcc/g++ podczas
kompilacji.

Po zainstalowaniu tego pakietu przeczytaj %{_defaultdocdir}/INSTALL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install colorgcc $RPM_BUILD_ROOT%{_bindir}

gzip -9nf INSTALL ChangeLog CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz colorgccrc
%attr(755,root,root) %{_bindir}/colorgcc
