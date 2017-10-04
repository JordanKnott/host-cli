import click
from subprocess import call


def load_rules():
    with open("C:\Windows\System32\drivers\etc\hosts") as file:
        contents = file.readlines();

        rules = []
        for line in contents:
            if not line.startswith("#") and not line.strip() == "":
                print(parts)
                rule = {
                        "ip" : parts[0].strip(),
                        "domain" : parts[1].strip()
                        }
                rules.append(rule)

        return rules
                
def save_rules(rules):
    with open("C:\Windows\System32\drivers\etc\hosts", "w") as file:
        for rule in rules:
            file.write("{}\t{}\n".format(rule["ip"], rule["domain"]))

def add_rule(rules, ip, domain):
    rules.append({
        "ip" : ip,
        "domain" : domain
        })
    return rules


@click.group()
def rules():
    """Command line utility script to add/remove/view DNS rules in the hosts file"""
    pass


@click.command()
def purge():
    """Purges all rules from the host file. Use with caution."""
    rules = load_rules()
    for rule in rules:
        print("Purging {} - {}".format(rule['ip'], rule['domain']))
    rules = []
    save_rules(rules)

@click.command()
@click.argument("domain")
@click.argument("ip")
@click.option("--www/--no-www", default=False, help="Adds a second rule that prepends 'www.' to the given domain")
def add(domain, ip, www):
    """Add a rule to the hosts file"""
    rules = load_rules()
    add_rule(rules, ip, domain)
    if www:
        add_rule(rules, ip, "www." + domain)
    save_rules(rules)
    

def flush_dns():
    call(["ipconfig", "/flushdns"])


@click.command()
@click.argument("domain")
@click.option("--www/--no-www", default=False, help="Remove a 'www' version of the domain, if it exists")
def remove(domain, www):
    """Remove a rule in the hosts file that has the given domain"""
    rules = load_rules()
    slated_for_removal = []
    for rule in rules:
        if rule['domain'] == domain:
            print("Removing {} - {}".format(rule['ip'], rule['domain']))
            slated_for_removal.append(rule)
        if www and rule['domain'] == "www." + domain:
            print("Removing {} - {}".format(rule['ip'], rule['domain']))
            slated_for_removal.append(rule)
    for slated in slated_for_removal:
        rules.remove(slated)
    save_rules(rules)


@click.command("list")
def list_rules():
    """View all of the rules in the host file"""
    print("{:<30}{:<30}".format("IP Address", "Domain"))
    for rule in load_rules():
        print("{:<30}{:<30}".format(rule['ip'], rule['domain']))


rules.add_command(add)
rules.add_command(remove)
rules.add_command(list_rules)
rules.add_command(purge)

if __name__ == "__main__":
    rules()
