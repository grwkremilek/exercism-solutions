#pragma once

namespace space_age {
	class space_age {
	private:
		const unsigned long long m_seconds;
		float on_another_planet(float orbitalPeriod) const;
	public:
		explicit space_age(unsigned long long seconds) : m_seconds(seconds) {
		}
		unsigned long long seconds() const;
		float on_earth() const;
		float on_mercury() const;
		float on_venus() const;
		float on_mars() const;
		float on_jupiter() const;
		float on_saturn() const;
		float on_uranus() const;
		float on_neptune() const;
	};
}
