%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.83
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Ace/AcePerl-%{version}.tar.gz
Patch0:		%{name}-defaults.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcePerl provides an interface to the ACEDB object-oriented database.

%description -l pl
AcePerl umo¿liwia dostêp do obiektowej bazy danych ACEDB.

%package -n perl-AceBrowser
Summary:	AceBrowser perl module
Summary(pl):	Modu³ perla AceBrowser
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	apache

%description -n perl-AceBrowser

%description -n perl-AceBrowser -l pl

%prep
%setup -q -n AcePerl-%{version}
%patch -p0

%build
# Makefile.PL does not read from non-terminal stdin
%{__perl} Makefile.PL < /dev/null
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd,/home/httpd/{cgi-bin,html}}/ace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README DISCLAIMER.txt
%{perl_sitearch}/Ace.pm
%dir %{perl_sitearch}/Ace
%{perl_sitearch}/Ace/[^B]*
%{perl_sitearch}/GFF
%{perl_sitearch}/auto/Ace
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/Ace.3pm*
%{_mandir}/man3/Ace::[^B]*

%files -n perl-AceBrowser
%defattr(644,root,root,755)
%doc README.ACEBROWSER
%dir %{_sysconfdir}/httpd/ace
%dir /home/httpd/cgi-bin/ace
%dir /home/httpd/html/ace
%{perl_sitearch}/Ace/Browser
%{_mandir}/man3/Ace::B*
