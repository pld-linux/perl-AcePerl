%include	/usr/lib/rpm/macros.perl
%define	pdir	Ace
Summary:	AcePerl - Perl interface for the ACEDB object-oriented database
Summary(pl.UTF-8):   AcePerl - interfejs perlowy do obiektowej bazy danych ACEDB
Name:		perl-AcePerl
Version:	1.89
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/AcePerl-%{version}.tar.gz
# Source0-md5:	547da3ca59894e99448408cfe9a8ae6e
Patch0:		%{name}-defaults.patch
Patch1:		%{name}-path.patch
BuildRequires:	cpp
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GD
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcePerl provides an interface to the ACEDB object-oriented database.
Designed specifically for use in genome sequencing projects, ACEDB
provides powerful modeling and management services for biological and
laboratory data. For others, it is a good open source introduction to
the world of object-oriented databases.

%description -l pl.UTF-8
AcePerl umożliwia dostęp do obiektowej bazy danych ACEDB. Został
zaprojektowany dla projektów dotyczących genomów. ACEDB udostępnia
potężne usługi modelowania i zarządzania danymi biologicznymi i
laboratoryjnymi. Ponadto, jest on dobrym wprowadzeniem otwartego
oprogramowania w swiat baz obiektowych.

%package -n perl-AceBrowser
Summary:	AceBrowser - collection of CGI scripts providing interface to ACEDB
Summary(pl.UTF-8):   AceBrowser - zbiór skryptów CGI stanowiących interfejs do ACEDB
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	webserver = apache

%description -n perl-AceBrowser
AceBrowser is a collection of CGI scripts that run on top of AcePerl
to provide a simple browsable interface to ACEDB databases. Some of
the code has been tuned for the C. elegans database, but most of it is
fully generic.

%description -n perl-AceBrowser -l pl.UTF-8
AceBrowser jest zbiorem skryptów CGI, działających w oparciu o AcePerl
i stanowiących prosty interfejs do baz danych ACEDB. Część kodu
zoptymalizowano dla bazy danych C. elegans, lecz większość jest
ogólna.

%prep
%setup -q -n AcePerl-%{version}
%patch0 -p0
%patch1 -p1

%build
# Makefile.PL does not read from non-terminal stdin
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags} -fPIC"
cd RPC
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags} -fPIC"
cd ../Freesubs
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd RPC
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../Freesubs
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd,/home/services/httpd/{cgi-bin,html}}/ace
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Ace/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Ace/Freesubs/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Ace/RPC/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README DISCLAIMER.txt
%attr(755,root,root) %{_bindir}/ace.pl
%{perl_vendorlib}/Ace.pm
%dir %{perl_vendorlib}/Ace
%{perl_vendorlib}/Ace/[!B]*
%{perl_vendorlib}/GFF
%{perl_vendorlib}/auto/Ace
%dir %{perl_vendorarch}/Ace
%{perl_vendorarch}/Ace/*.pm
%dir %{perl_vendorarch}/auto/Ace
%dir %{perl_vendorarch}/auto/Ace/Freesubs
%{perl_vendorarch}/auto/Ace/Freesubs/Freesubs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Ace/Freesubs/Freesubs.so
%dir %{perl_vendorarch}/auto/Ace/RPC
%{perl_vendorarch}/auto/Ace/RPC/RPC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Ace/RPC/RPC.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/ace.pl*
%{_mandir}/man3/Ace.3pm*
%{_mandir}/man3/Ace::[!B]*

%files -n perl-AceBrowser
%defattr(644,root,root,755)
%doc README.ACEBROWSER
%dir %{_sysconfdir}/httpd/ace
%dir /home/services/httpd/cgi-bin/ace
%dir /home/services/httpd/html/ace
%{perl_vendorlib}/Ace/Browser
%{_mandir}/man3/Ace::B*
