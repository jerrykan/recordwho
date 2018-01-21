The very very basic guide to getting going...

Set up the virtualenv:

  # cd <path to recordwho>
  # python3 -m venv venv
  # source venv/bin/activate
  # pip install -r requirements.txt

Start Errbot to record the WHO data:

  # errbot

Generate pretty charts:

  # python scripts/who_to_d3json.py
  # cd html
  # python -m http.server


= General Notes =
Errbot is used to connect to IRC, with the `recordwho` plugin in the `plugins`
directory used to record the WHO data of all users in the channels configured in
`config.py`.

These channels are also hard-coded in coded in `scripts/who_to_d3json.py` and
the `id` values of the svg elements on `html/index.html`

Some of how all this is done could be a lot cleaner, but given this was intended
as a quick and dirty one-off not a lot of effort was put into anything other
than making it work.
