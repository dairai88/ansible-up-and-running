## list available plugins related to inventory

```zsh
ansible-doc -t inventory -l
```

## check usage of a specific plugin

```zsh
ansible-doc -t inventory amazon.aws.aws_ec2
```

## test dynamic inventory configuation by listing ec2 instances

```zsh
ansible-inventory -i inventory/aws_ec2.yaml --list
```

## test ping module with aws credential

```zsh
ansible all -u ec2-user --private-key /Users/daleisun/Downloads/MyAnsiblePair.pem -i inventory/aws_ec2.yaml -m ping
```

## run playbook with aws credential

```zsh
ansible-playbook -u ec2-user --private-key /Users/daleisun/Downloads/MyAnsiblePair.pem test_dynamic_inventory.yaml
```
