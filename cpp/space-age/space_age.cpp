#include "space_age.h"

constexpr float earthYearInSeconds = 31557600.0f;

unsigned long long space_age::space_age::seconds() const
{
	return m_seconds;
}

float space_age::space_age::on_another_planet(float orbitalPeriod) const
{
	float ageOnEarth = m_seconds / earthYearInSeconds;
	float ageOnAnotherPlanet = ageOnEarth / orbitalPeriod;

	return ageOnAnotherPlanet;
}

float space_age::space_age::on_earth() const
{
	return on_another_planet(1.0f);
}

float space_age::space_age::on_mercury() const
{
	return on_another_planet(0.2408467f);
}

float space_age::space_age::on_venus() const
{
	return on_another_planet(0.61519726f);
}

float space_age::space_age::on_mars() const
{
	return on_another_planet(1.8808158f);
}

float space_age::space_age::on_jupiter() const
{
	return on_another_planet(11.862615f);
}

float space_age::space_age::on_saturn() const
{
	return on_another_planet(29.447498f);
}

float space_age::space_age::on_uranus() const
{
	return on_another_planet(84.016846f);
}

float space_age::space_age::on_neptune() const
{
	return on_another_planet(164.79132f);
}
