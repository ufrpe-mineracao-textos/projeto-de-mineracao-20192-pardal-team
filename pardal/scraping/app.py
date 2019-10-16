import twint

c = twint.Config()

c.Search = '#politica'
c.Format = 'Tweet id: {id} | Tweet: {tweet}'
c.Lang = 'pt'
c.Limit = 5000
c.Output = 'datasets/politics'
c.Store_csv = True

twint.run.Search(c)
