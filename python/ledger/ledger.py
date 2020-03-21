from datetime import datetime

FORMAT = {
    'en_US': 
                {
                    'title' : 'Date       | Description               | Change       ',
                    'date'  : lambda x      :  f'{x:%m/%d/%Y}',
                    'change': lambda x, y   : (lambda i: (f'{y}{i} ', f'({y}{i})')[x < 0])(f'{abs(x / 100):,.2f}')
                },
    'nl_NL':    {
                    'title' : 'Datum      | Omschrijving              | Verandering  ',
                    'date'  : lambda x      : f'{x:%d-%m-%Y}',
                    'change': lambda x, y   : f'{y} {x / 100:_.2f} '.replace('.', ',').replace('_', '.')
                },
    'USD': '$',
    'EUR': '€'
}


class LedgerEntry(object):
    def __lt__(self, o):
        if self.date < o.date:
            return True
        if self.description < o.description:
            return True
        return self.change < o.change


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    result = [FORMAT[locale]['title']]

    for entry in sorted(entries):
        date = FORMAT[locale]['date'](entry.date)
        description = (lambda x: (f'{x:25}', x[:22] + '...')[len(x) > 25])(entry.description)
        change = FORMAT[locale]['change'](entry.change, FORMAT[currency])

        result.append(f'{date} | {description} | {change:>13}')
    return '\n'.join(result)
