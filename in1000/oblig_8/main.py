from node import Node
from regneklynge import Regneklynge


if __name__ == '__main__':
    abel = Regneklynge(12)
    for _ in range(650):
        abel.settInnNode(Node(64, 1))

    for _ in range(16):
        abel.settInnNode(Node(1024, 2))

    print('\nTesting without input file:')
    print('Nodes with minimum 32GB: {}.'.format(abel.noderMedNokMinne(32)))
    print('Nodes with minimum 64GB: {}.'.format(abel.noderMedNokMinne(64)))
    print('Nodes with minimum 128GB: {}.'.format(abel.noderMedNokMinne(128)))
    print('Number of CPUs: {}.'.format(abel.antProsessorer()))
    print('Number of racks: {}.'.format(abel.antRacks()))

    abel2 = Regneklynge('config.txt')
    print('\nTesting with input file:')
    print('Nodes with minimum 32GB: {}.'.format(abel2.noderMedNokMinne(32)))
    print('Nodes with minimum 64GB: {}.'.format(abel2.noderMedNokMinne(64)))
    print('Nodes with minimum 128GB: {}.'.format(abel2.noderMedNokMinne(128)))
    print('Number of CPUs: {}.'.format(abel2.antProsessorer()))
    print('Number of racks: {}.'.format(abel2.antRacks()))
