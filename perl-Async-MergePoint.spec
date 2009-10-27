#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Async
%define	pnam	MergePoint
Summary:	Async::MergePoint - resynchronise diverged control flow
#Summary(pl.UTF-8):
Name:		perl-Async-MergePoint
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Async-MergePoint-%{version}.tar.gz
# Source0-md5:	f4a6f9a9dc0a1748f503c01893d544cc
URL:		http://search.cpan.org/dist/Async-MergePoint/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Often in program logic, multiple different steps need to be taken that
are independent of each other, but their total result is needed before
the next step can be taken. In synchonous code, the usual approach is
to do them sequentially.

An asynchronous or event-based program could do this, but if each step
involves some IO idle time, better overall performance can often be
gained by running the steps in parallel. A Async::MergePoint object
can then be used to wait for all of the steps to complete, before
passing the combined result of each step on to the next stage.

A merge point maintains a set of outstanding operations it is waiting
on; these are arbitrary string values provided at the object's
construction. Each time the done() method is called, the named item is
marked as being complete. When all of the required items are so
marked, the on_finished continuation is invoked.

For use cases where code may be split across several different lexical
scopes, it may not be convenient or possible to share a lexical
variable, to pass on the result of some asynchronous operation. In
these cases, when an item is marked as complete a value can also be
provided which contains the results of that step. The on_finished
callback is passed a hash (in list form, rather than by reference) of
the collected item values.

This module was originally part of the IO::Async distribution, but was
removed under the inspiration of Pedro Melo's Async::Hooks
distribution, because it doesn't itself contain anything IO-specific.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Async
%{perl_vendorlib}/Async/*.pm
%{_mandir}/man3/*
