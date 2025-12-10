# 🌐 Infrastructure Documentation: {{ client_name }}

## 1. Project Overview
| Attribute | Detail |
| :--- | :--- |
| **Client** | {{ client_name }} |
| **Engineer** | {{ engineer_name }} |
| **Date** | {{ deployment_date }} |
| **Region** | {{ location }} |

---

## 2. Network Topology
The core infrastructure relies on a Hub VNet topology.

### Virtual Network
* **CIDR:** `{{ vnet_cidr }}`

### Subnets
| Name | CIDR | Purpose |
| :--- | :--- | :--- |
{% for subnet in subnets -%}
| **{{ subnet.name }}** | `{{ subnet.cidr }}` | {{ subnet.purpose }} |
{% endfor %}

---

## 3. Connectivity
### VPN Gateway
* **SKU:** {{ vpn_sku }}
* **Type:** RouteBased
* **Public IP:** *(To be filled after deployment)*

### Peering (ACTION REQUIRED)
* [ ] Peer with Client Legacy VNet (if applicable)
* [ ] Peer with MSP Management VNet

---

## 4. Maintenance
To deploy changes to this infrastructure, update the `main.tf` file in this repository and run the standard pipeline. **Do not make manual changes in the Azure Portal.**
