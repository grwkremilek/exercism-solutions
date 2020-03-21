import java.time.LocalDate;
import java.time.LocalDateTime;

class Gigasecond {
    private LocalDateTime startTime;

    Gigasecond(LocalDate birthDate) {
        this.startTime = birthDate.atStartOfDay();
    }

    Gigasecond(LocalDateTime birthDateTime) {
        this.startTime = birthDateTime;
    }

    LocalDateTime getDateTime() {
        return startTime.plusSeconds(1000000000);
    }

}
