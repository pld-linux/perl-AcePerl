%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.86
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Ace/AcePerl-%{version}.tar.gz
# Source0-md5:	133664b68a2a97c9f3c8cd7096ba472b
Patch0:		%{name}-defaults.patch
Patch1:		%{name}-path.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.1-13
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
%patch0 -p0
%patch1 -p1

%build
# Makefile.PL does not read from non-terminal stdin
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"
cd RPC
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"
cd ../Freesubs
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd RPC
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../Freesubs
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ..

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/httpd,/home/httpd/{cgi-bin,html}}/ace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README DISCLAIMER.txt
%attr(755,root,root) %{_bindir}/ace.pl
%{perl_vendorlib}/Ace.pm
%dir %{perl_vendorlib}/Ace
%{perl_vendorlib}/Ace/[^B]*
%{perl_vendorlib}/GFF
%{perl_vendorlib}/auto/Ace
%dir %{perl_vendorarch}/Ace
%{perl_vendorarch}/Ace/*.pm
%dir %{perl_vendorarch}/auto/Ace
%{perl_vendorarch}/auto/Ace/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/ace.pl*
%{_mandir}/man3/Ace.3pm*
%{_mandir}/man3/Ace::[^B]*

%files -n perl-AceBrowser
%defattr(644,root,root,755)
%doc README.ACEBROWSER
%dir %{_sysconfdir}/httpd/ace
%dir /home/httpd/cgi-bin/ace
%dir /home/httpd/html/ace
%{perl_vendorlib}/Ace/Browser
%{_mandir}/man3/Ace::B*
