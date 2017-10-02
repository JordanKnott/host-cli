import click
from subprocess import call


def load_rules():
    with open("C:\Windows\System32\drivers\etc\hosts") as file:
        contents = file.readlines();

        rules = []
        for line in contents:
            if not line.startswith("#") and not line.strip() == "":
                parts = line.split("\t")
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
@click.argument("ip")
@click.argument("domain")
def add(ip, domain):
    """Add a rule to the hosts file"""
    rules = load_rules()
    add_rule(rules, ip, domain)
    save_rules(rules)
    

def flush_dns():
    call(["ipconfig", "/flushdns"])


@click.command()
@click.argument("domain")
def remove(domain):
    """Remove a rule in the hosts file that has the given domain"""
    rules = load_rules()
    for rule in rules:
        if rule['domain'] == domain:
            print("Removing {} - {}".format(rule['ip'], rule['domain']))
            rules.remove(rule)
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

if __name__ == "__main__":
    rules()
