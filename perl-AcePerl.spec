%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.64
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/AcePerl-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcePerl provides an interface to the ACEDB object-oriented database.

%description -l pl
AcePerl umo¿liwia dostêp do obiektowej bazy danych ACEDB.

%prep
%setup -q -n AcePerl-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Ace/Freesubs/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Ace
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitearch}/Ace.pm
%{perl_sitearch}/GFF

%dir %{perl_sitearch}/Ace
%{perl_sitearch}/Ace/*.pm
%dir %{perl_sitearch}/Ace/Sequence
%{perl_sitearch}/Ace/Sequence/*.pm

%dir %{perl_sitearch}/auto/Ace
%{perl_sitearch}/auto/Ace/*.al
%{perl_sitearch}/auto/Ace/autosplit.ix
%{perl_sitearch}/auto/Ace/.packlist
%dir %{perl_sitearch}/auto/Ace/Freesubs
%{perl_sitearch}/auto/Ace/Freesubs/Freesubs.bs
%attr(755,root,root) %{perl_sitearch}/auto/Ace/Freesubs/Freesubs.so
%{perl_sitearch}/auto/Ace/Object
%{perl_sitearch}/auto/Ace/Sequence

%{_prefix}/src/examples/%{name}-%{version}

%{_mandir}/man3/*
