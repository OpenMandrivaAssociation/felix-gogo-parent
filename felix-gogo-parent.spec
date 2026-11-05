%global project   felix-gogo
%global pkgname   parent

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{project}-%{pkgname}}

Name:             %{?scl_prefix}%{project}-%{pkgname}
Version:          7
Release:          1
Summary:          Parent package for Felix Gogo
Group:            Development/Java
License:          ASL 2.0
URL:              https://felix.apache.org/site/apache-felix-gogo.html

Source0:          https://repo1.maven.org/maven2/org/apache/felix/gogo-parent/%{version}/gogo-parent-%{version}.pom
Source1:          https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	validate

%{?scl:Requires: %scl_runtime}

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# felix-parent 8 is not packaged. The groupId lived there. The bundle
# plugin is marked as an extension, so Maven would resolve it while
# reading the POM. Version 6.0.0 is not packaged.
sed -i '/<parent>/,/<\/parent>/d' pom.xml
sed -i 's|<modelVersion>4.0.0</modelVersion>|<modelVersion>4.0.0</modelVersion>\n    <groupId>org.apache.felix</groupId>|' pom.xml
sed -i '/<extensions>true<\/extensions>/d' pom.xml

%files -f .mfiles
%doc LICENSE
