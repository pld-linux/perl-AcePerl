%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.54
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/AcePerl-%{version}.tar.gz
Patch:		perl-AcePerl-paths.patch
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-12
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
AcePerl provides an interface to the ACEDB object-oriented database.

%description -l pl
AcePerl umo¿liwia dostêp do obiektowej bazy danych ACEDB.

%prep
%setup -q -n AcePerl-%{version}
%patch -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Ace/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Ace
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitearch}/Ace.pm
%{perl_sitearch}/Ace/*.pm

%dir %{perl_sitearch}/auto/Ace
%{perl_sitearch}/auto/Ace/Object
%{perl_sitearch}/auto/Ace/*.al
%{perl_sitearch}/auto/Ace/autosplit.ix
%{perl_sitearch}/auto/Ace/.packlist
%{perl_sitearch}/auto/Ace/Ace.bs
%attr(755,root,root) %{perl_sitearch}/auto/Ace/Ace.so

%dir /usr/src/examples/%{name}-%{version}
%attr(755,root,root) /usr/src/examples/%{name}-%{version}/*.pl

%{_mandir}/man3/*
