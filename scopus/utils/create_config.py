from sys import version_info

py3 = version_info >= (3, 0)


def set_authentication(config, fname):
    """Create section Authentication in config file and add API Key to it."""
    try:
        config.add_section('Authentication')
    except configparser.DuplicateSectionError:
        pass
    # APIKey
    prompt_key = ("Please enter your API Key, obtained from "
                  "http://dev.elsevier.com/myapikey.html: \n")
    if py3:
        key = input(prompt_key)
    else:
        key = raw_input(prompt_key)
    config.set('Authentication', 'APIKey', key)
    # InstToken
    prompt_token = ("API Keys are sufficient for most users.  If you have to "
                    "use Authtoken authentication, please enter the token, "
                    "otherwise press enter: \n")
    if py3:
        token = input(prompt_token)
    else:
        token = raw_input(prompt_token)
    if len(token) > 0:
        config.set('Authentication', 'InstToken', token)
    # Write out
    with open(fname, 'w') as f:
        config.write(f)
