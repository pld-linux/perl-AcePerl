%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.83
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Ace/AcePerl-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcePerl provides an interface to the ACEDB object-oriented database.

%description -l pl
AcePerl umo¿liwia dostêp do obiektowej bazy danych ACEDB.

%prep
%setup -q -n AcePerl-%{version}

%build
echo "3" | perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.ACEBROWSER DISCLAIMER.txt
%{_mandir}/man3/*

%{perl_sitearch}/Ace.pm
%{perl_sitearch}/Ace
%{perl_sitearch}/GFF
%{perl_sitearch}/auto/Ace
%{_examplesdir}/%{name}-%{version}
