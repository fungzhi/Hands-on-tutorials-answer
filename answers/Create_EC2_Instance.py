from aws_cdk import core
import aws_cdk.aws_ec2 as ec2



ec2_type = "t2.micro"
key_name = "id_rsa"  # Setup key_name for EC2 instance login 
linux_ami = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                 )



class ec2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        vpc=ec2.Vpc(self, 'default')

        # Create Bastion
        bastion = ec2.BastionHostLinux(self, "myBastion",
                                       vpc=vpc,
                                       subnet_selection=ec2.SubnetSelection(
                                           subnet_type=ec2.SubnetType.PUBLIC),
                                       instance_name="myBastionHostLinux",
                                       instance_type=ec2.InstanceType(instance_type_identifier="t2.micro"))
        


        bastion.connections.allow_from_any_ipv4(
            ec2.Port.tcp(22), "Internet access SSH")
            
            